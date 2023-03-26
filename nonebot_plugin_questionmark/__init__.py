from nonebot import on_message
from nonebot.adapters.onebot.v11 import MessageEvent


question = on_message()


@question.handle()
async def _(event: MessageEvent):
    if event.message.extract_plain_text() in {"?", "？"}:
        await question.send("¿")
