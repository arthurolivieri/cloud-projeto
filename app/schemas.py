from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class LoginRequest(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    jwt: str

class TokenData(BaseModel):
    email: str

class Joke(BaseModel):
    setup: str
    delivery: str