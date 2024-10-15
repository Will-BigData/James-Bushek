import mysql.connector


class Skill():
    def __init__(self, skill_name, equipable="", multiplier=0, cooldown=0) -> None:
        self.skill_name = skill_name
        self.equipable = equipable
        self.multiplier = multiplier
        self.cooldown = cooldown
        self.SetSkill(skill_name)

    def SetSkill(self, skill):
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")

        cursor.execute(f"SELECT * FROM Skills WHERE SkillName = '{skill}'")
        result = cursor.fetchall()

        self.skill_name = str(result[0][0])
        self.equipable = str(result[0][1])
        self.multiplier = int(result[0][2])
        self.cooldown = int(result[0][3])

        cursor.close()
        cnx.close()