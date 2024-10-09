

from typing import Any


class Weapon():
    def __init__(self, weapon_name, base_damage, auxillary) -> None:
        self.WeaponName = weapon_name
        self.BaseDamage = base_damage
        self.Auxillary = auxillary

    def __getattribute__(self, name: str) -> Any:
        pass

    def __setattr__(self, name: str, value: Any) -> None:
        pass