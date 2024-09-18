from fastapi import FastAPI, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from db.db import get_all_notes
from db.db import get_user
from db.db import add_note
from y_speller import spell_check

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
    raise HTTPException(status_code=403, detail="Not authorized")


@app.post("/notes")
def add_notes(note_data: str, api_token: str = Security(authorization)):
    user = get_user(api_token)
    if user:
        note_data = spell_check(note_data)
        if add_note(user, text_note=note_data):
            return {"message": "Note added successfully"}
        raise HTTPException(status_code=500, detail="Failed to add note")
    raise HTTPException(status_code=403, detail="Not authorized")
