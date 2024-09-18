import json


def get_all_notes(user: str) -> list:
    try:
        with open("db/note_data.json", "r", encoding="utf-8") as file_data:
            all_notes = json.load(file_data)
            return all_notes[user]
    except FileNotFoundError:
        return []


def get_user(token: str) -> str:
    try:
        with open("db/user_data.json", "r", encoding="utf-8") as file_data:
            all_users = json.load(file_data)
            if token in all_users:
                return all_users[token]["name"]
            else:
                return ""
    except FileNotFoundError:
        return ""

