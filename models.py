from pydantic import BaseModel


class NoteData(BaseModel):
    text_note: str


class User(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    token: str