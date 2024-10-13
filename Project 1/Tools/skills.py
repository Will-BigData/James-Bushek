

from typing import Any


class Skill():
    def __init__(self, skill_name, equipable, multiplier, cooldown) -> None:
        self.skill_name = skill_name
        self.equipable = equipable
        self.multiplier = multiplier
        self.cooldown = cooldown
        self.SetSkill(skill_name)

    def SetSkill(self, skill):
        pass