# FastAPI Postgres Docker template v0.0.1

## db/
Docker image for postgres database.
Set Password in Dockerfile.dev

## backend/
In `config/` folder create a `.env` file with this structure:

```bash
APP_ENV=DEVELOPMENT

# DB settings
DB_NAME=db_name
DB_PASS=postgres
DB_HOST=db
DB_PORT=5432
DB_USER=postgres

# APP SETTINGS

BASE_URL=localhost:3000/api/V1
PROJECT_NAME=name
VERSION=0.0.1
DESCRIPTION="New FastAPI, docker, tortoise/postgres Project"
APP_PORT=3000
APP_HOST=0.0.0.0
DEBUG=1
RELOAD=1
```

## Running the project in local

Create a Python virtual environment with `python3 -m venv venv` in the `backend/` folder.
If necessary, export a new `PYTHONPATH` with `export $PYTHONPATH=$PWD/` inside `backend/` folder
(to check `PYTHONPATH` -> `echo $PYTHONPATH`)

From root folder: `docker-compose up --build`

## Scripts

- `update_requirements.sh` Update the requirements in `requirements.txt` after installing new libraries
- `format.sh` run a style format in the `backend/` folder with autopep8 and pysort