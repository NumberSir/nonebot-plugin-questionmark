from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    qm_trigger_rate: float = 0.3  # 回复概率
    qm_enable_groups: list = []  # 白名单群聊


__all__ = [
    "Config"
]
