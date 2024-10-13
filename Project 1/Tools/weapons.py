import mysql.connector
from typing import Any


class Weapon():
    def __init__(self, weapon_name, base_damage, auxillary) -> None:
        self.weapon_name = weapon_name
        self.base_damage = base_damage
        self.auxillary = auxillary
        self.ChangeWeapon(weapon_name)

    def ChangeWeapon(self, weapon):
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")
        
        cursor.execute(f"SELECT * FROM Weapons WHERE WeaponName = {weapon}")
        result = cursor.fetchall()
        self = map(result)

        cursor.close()
        cnx.close()

    