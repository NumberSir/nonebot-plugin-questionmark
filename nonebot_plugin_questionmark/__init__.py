from nonebot import on_message
from nonebot.adapters import Event


question = on_message()


@question.handle()
async def _(event: Event):
    mark = event.get_plaintext().strip()
    if set(mark) <= {"?", "？", "¿", "!", "！", "¡"}:
        mark = mark\
            .replace("¿", "d").replace("?", "¿").replace("？", "¿").replace("d", "?")\
            .replace("¡", "d").replace("!", "¡").replace("！", "¡").replace("d", "!")
        await question.send(mark)
