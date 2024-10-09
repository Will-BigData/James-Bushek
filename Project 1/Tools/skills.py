

from typing import Any


class Skill():
    def __init__(self, skill_name, equipable, multiplier, cooldown) -> None:
        self.skill_name = skill_name
        self.equipable = equipable
        self.multiplier = multiplier
        self.cooldown = cooldown

    def __getattribute__(self, name: str) -> Any:
        pass

    def __setattr__(self, name: str, value: Any) -> None:
        pass