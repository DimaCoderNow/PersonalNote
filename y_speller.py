import aiohttp


speller_url = "https://speller.yandex.net/services/spellservice.json/checkText?text="


async def spell_check(text: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(speller_url + text) as res:
            if res.status == 200:
                wrong_words = await res.json()
                if wrong_words:
                    wrong_words.reverse()
                    for wrong_word in wrong_words:
                        start = wrong_word["pos"]
                        end = wrong_word["pos"] + wrong_word["len"]
                        text = text[:start] + wrong_word["s"][0] + text[end:]
    return text
