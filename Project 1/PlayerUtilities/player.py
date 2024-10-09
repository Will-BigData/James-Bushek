from typing import Any


class Player:
    def __init__(self, weapon:str, aux_weapon:int, skills:list, health_max:int, current_health:int) -> None:
        self.weapon = weapon
        self.aux_weapon = aux_weapon
        self.skills = skills
        self.health_max = health_max
        self.current_health = current_health
    
    def ImproveHealth(self):
        self.health_max += 3

    def Heal(self):
        self.current_health = self.health_max/1

    # TODO: getters and setters
    def __getattribute__(self, name: str) -> Any:
        pass

    def __setattr__(self, name: str, value: Any) -> None:
        pass