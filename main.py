from fastapi import FastAPI, Security
from fastapi.security.api_key import APIKeyHeader

from db.db import get_all_notes
from db.db import get_user

app = FastAPI()
authorization = APIKeyHeader(name="Authorization")


@app.get("/")
async def read_root():
    return "Hello production!"


@app.get("/notes")
def read_notes(api_token: str = Security(authorization)):
    user = get_user(api_token)
    if user:
        return get_all_notes(user)
    return []
