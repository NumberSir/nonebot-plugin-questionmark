from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent


question = on_message()


@question.handle()
async def _(event: MessageEvent):
    mark = event.message.extract_plain_text().strip()
    if all(_ in {"?", "？", "¿"} for _ in set(mark)):
        mark = mark.replace("¿", "d").replace("?", "¿").replace("？", "¿").replace("d", "?")
        await question.send(mark)
