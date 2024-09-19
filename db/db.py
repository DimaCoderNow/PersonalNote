import json


def get_all_notes(user: str) -> list:
    try:
        with open("db/note_data.json", "r", encoding="utf-8") as file_data:
            all_notes = json.load(file_data)
            return all_notes[user]
    except FileNotFoundError:
        return []


def add_note(user: str, text_note: str) -> bool:
    try:
        with open("db/note_data.json", "r", encoding="utf-8") as file_data:
            all_notes = json.load(file_data)
            if user in all_notes:
                all_notes[user].append(text_note)
                try:
                    with open("db/note_data.json", "w", encoding="utf-8") as new_data:
                        json.dump(all_notes, new_data, indent=4)
                        return True
                except FileNotFoundError:
                    return False
            return False
    except FileNotFoundError:
        return False


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


def get_token(name: str, pwd: str) -> str:
    try:
        with open("db/user_data.json", "r", encoding="utf-8") as file_data:
            all_users = json.load(file_data)
            if all_users:
                for token, user in all_users.items():
                    if user["name"] == name and user["password"] == pwd:
                        return token
            else:
                return ""
    except FileNotFoundError:
        return ""
