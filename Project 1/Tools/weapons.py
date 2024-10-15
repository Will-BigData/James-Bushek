import mysql.connector


class Weapon():
    def __init__(self, weapon_name, base_damage=0, auxillary=False) -> None:
        self.weapon_name = weapon_name
        self.base_damage = base_damage
        self.auxillary = auxillary
        self.ChangeWeapon(weapon_name)

    def ChangeWeapon(self, weapon):
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")
        if self.weapon_name != "none":
            cursor.execute(f"SELECT * FROM Weapons WHERE WeaponName = '{weapon}'")
            result = cursor.fetchall()

            self.weapon_name = str(result[0][0])
            self.base_damage = int(result[0][1])
            self.auxillary = bool(result[0][2])

        cursor.close()
        cnx.close()

    