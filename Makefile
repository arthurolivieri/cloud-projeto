start-dev:
	uvicorn app.main:app --reload

start:
	uvicorn app.main:app

psql-up:
	docker compose -f docker-compose.yaml up -d --build --force-recreate --remove-orphans db

psql-down:
	docker compose -f docker-compose.yaml down -v --remove-orphans