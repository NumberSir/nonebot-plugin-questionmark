from nonebot import on_regex
from nonebot.params import RegexGroup
from nonebot.exception import IgnoredException


question = on_regex(r"^([?？¿!！¡\s])+$", priority=5, block=False)


@question.handle()
async def _(rgx: tuple = RegexGroup()):
    if not rgx:
        raise IgnoredException
    mark = rgx[0]\
        .replace("¿", "d").replace("?", "¿").replace("？", "¿").replace("d", "?")\
        .replace("¡", "d").replace("!", "¡").replace("！", "¡").replace("d", "!")
    await question.send(mark)
