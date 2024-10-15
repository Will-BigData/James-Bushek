import mysql.connector
from Tools.skills import Skill

class Shop:
    def __init__(self, player_skills, skill_list = [], weapon_list = []) -> None:
        self.skill_list = skill_list
        self.weapon_list = weapon_list
        self.player_skills = player_skills
        self.SetWeaponList()
        self.UpdateSkillList(player_skills)

    def UpdateSkillList(self, player_skills):
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")

        cursor.execute("SELECT SkillName FROM Skills")
        rows = cursor.fetchall()

        skill_list = []
        

        for row in rows:
            skill_valid = 0
            cleaned = str(row)[2:-3]
            for skill in player_skills:

                if skill.__getattribute__("skill_name") != cleaned:
                    skill_valid += 1

            if skill_valid == player_skills.__len__():
                skill_list.append(cleaned)

        self.skill_list = skill_list

        cursor.close()
        cnx.close()

    def SetWeaponList(self):
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")

        cursor.execute("SELECT WeaponName FROM Weapons")
        rows = cursor.fetchall()

        weapon_list = []

        for row in rows:
            cleaned = str(row)[2:-3]
            weapon_list.append(cleaned)

        self.weapon_list = weapon_list

        cursor.close()
        cnx.close()