from fastapi import FastAPI, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel

from db.db import get_all_notes, get_token
from db.db import get_user
from db.db import add_note
from y_speller import spell_check

app = FastAPI()
authorization = APIKeyHeader(name="Authorization")


class NoteData(BaseModel):
    text_note: str


class User(BaseModel):
    name: str
    password: str


@app.get("/")
async def read_root():
    return "Hello production!"


@app.get("/notes")
def read_notes(api_token: str = Security(authorization)) -> list[NoteData]:
    user = get_user(api_token)
    if user:
        notes = get_all_notes(user)
        notes_data = [NoteData(text_note=note) for note in notes]
        return notes_data
    raise HTTPException(status_code=403, detail="Not authorized")


@app.post("/notes")
def add_notes(note_data: NoteData, api_token: str = Security(authorization)):
    user = get_user(api_token)
    if user:
        note_data = spell_check(note_data.text_note)
        if add_note(user, text_note=note_data):
            return {"message": "Note added successfully"}
        raise HTTPException(status_code=500, detail="Failed to add note")
    raise HTTPException(status_code=403, detail="Not authorized")


@app.post("/login")
def user_login(user: User):
    if user:
        name = user.name
        password = user.password
        token = get_token(name, password)
        return {"token": token}
    raise HTTPException(status_code=401, detail="Unauthorized")
