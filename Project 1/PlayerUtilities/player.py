from typing import Any
from Tools.weapons import Weapon
from Tools.skills import Skill

class Player:
    def __init__(self, weapon:Weapon, aux_weapon:Weapon, skills:list, health_max:int, current_health:int, other_weapons:list) -> None:
        self.weapon = weapon
        self.aux_weapon = aux_weapon
        self.skills = skills
        self.health_max = health_max
        self.current_health = current_health
        self.other_weapons = other_weapons
    
    def ImproveHealth(self):
        self.health_max += 4

    def Heal(self):
        self.current_health = self.health_max/1
