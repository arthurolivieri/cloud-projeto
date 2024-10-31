from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from . import actions, models, schemas
from .database import SessionLocal, engine
from datetime import timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
import httpx

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

security = HTTPBearer()

@app.post("/registrar", response_model=schemas.Token)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = actions.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="Esse usuário já está registrado")
    
    created_user = actions.create_user(db=db, user=user)
    access_token = actions.create_access_token(
        data={"sub": created_user.email},
    )
    
    return {"jwt": access_token}

@app.post("/login", response_model=schemas.Token)
def login_for_access_token(
    login_data: schemas.LoginRequest,
    db: Session = Depends(get_db)
):
    user = actions.get_user_by_email(db, email=login_data.email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not actions.verify_password(login_data.senha, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = actions.create_access_token(
        data={"sub": user.email},
    )
    
    return {"jwt": access_token}

@app.get("/consultar", response_model=schemas.Joke, dependencies=[Depends(security)])
def consulta_api(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acesso negado: Token ausente ou inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, actions.SECRET_KEY, algorithms=[actions.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception

    user = actions.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    
    response = httpx.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch joke from external API")
    
    joke_data = response.json()
    joke_data = {
        "setup": joke_data["setup"],
        "delivery": joke_data["delivery"]
    }

    return joke_data