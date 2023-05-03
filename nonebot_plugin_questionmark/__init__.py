import contextlib
import random

from nonebot import on_regex, get_driver
from nonebot.exception import IgnoredException
from nonebot.internal.adapter import Event
from nonebot.params import RegexGroup

from .config import *

with contextlib.suppress(ImportError):
    from nonebot.adapters.onebot.v11 import GroupMessageEvent as Event
cfg = Config.parse_obj(get_driver().config.dict())


async def trigger_rule(event: Event) -> bool:
    with contextlib.suppress(AttributeError, NotImplementedError):
        if event.group_id not in cfg.qm_enable_groups and "all" not in cfg.qm_enable_groups:
            return False
    return random.random() <= cfg.qm_trigger_rate


question = on_regex(r"^([?？¿!！¡\s]+)$", priority=5, block=False, rule=trigger_rule)


@question.handle()
async def _(rgx: tuple = RegexGroup()):
    if not rgx:
        raise IgnoredException
    mark = rgx[0] \
        .replace("¿", "d").replace("?", "¿").replace("？", "¿").replace("d", "?") \
        .replace("¡", "d").replace("!", "¡").replace("！", "¡").replace("d", "!")
    await question.send(mark)
