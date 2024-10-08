from fastapi import FastAPI, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from db.db import get_all_notes, get_token
from db.db import get_user
from db.db import add_note

from models import *

from y_speller import spell_check

app = FastAPI()
authorization = APIKeyHeader(name="Authorization")


@app.get("/")
async def read_root():
    return "Hello production!"


@app.get("/notes")
async def read_notes(api_token: str = Security(authorization)) -> list[NoteData]:
    user = await get_user(api_token)
    if user:
        notes = await get_all_notes(user)
        notes_data = [NoteData(text_note=note) for note in notes]
        return notes_data
    raise HTTPException(status_code=403, detail="Not authorized")


@app.post("/notes")
async def add_notes(note_data: NoteData, api_token: str = Security(authorization)):
    user = await get_user(api_token)
    if user:
        note_data = await spell_check(note_data.text_note)
        if await add_note(user, text_note=note_data):
            return {"message": "Note added successfully"}
        raise HTTPException(status_code=500, detail="Failed to add note")
    raise HTTPException(status_code=403, detail="Not authorized")


@app.post("/login")
async def user_login(user: User) -> Token:
    if user:
        name = user.name
        password = user.password
        token = await get_token(name, password)
        if token:
            return Token(token=token)
    raise HTTPException(status_code=401, detail="Unauthorized")
