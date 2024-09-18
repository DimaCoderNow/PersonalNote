import requests

speller_url = "https://speller.yandex.net/services/spellservice.json/checkText?text="


def spell_check(text: str) -> str:
    res = requests.get(speller_url + text)
    if res.status_code == 200:
        wrong_words = res.json()
        if wrong_words:
            wrong_words.reverse()
            for wrong_word in wrong_words:
                start = wrong_word["pos"]
                end = wrong_word["pos"] + wrong_word["len"]
                text = text[:start] + wrong_word["s"][0] + text[end:]
    return text
