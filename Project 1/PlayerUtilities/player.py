import random
from Tools.weapons import Weapon
from Tools.skills import Skill

class Player:
    def __init__(self, weapon:Weapon, aux_weapon:Weapon, skills:list, health_max:int, current_health:int, all_weapons:list) -> None:
        self.weapon = weapon
        self.aux_weapon = aux_weapon
        self.skills = skills
        self.health_max = health_max
        self.current_health = current_health
        self.all_weapons = all_weapons
    
    def ImproveHealth(self):
        health = self.health_max
        health += 4
        self.health_max = health

    def Heal(self):
        self.current_health = 1+self.health_max-1

    def ChangeWeapon(self, name):
        new_weapon = Weapon(name)
        self.weapon = new_weapon

    def ChangeAuxWeapon(self, name):
        new_aux_weapon = Weapon(name)
        self.aux_weapon = new_aux_weapon

    def RandomAttack(self, skills):
        num_skills = skills.__len__()
        skill_rand = 0
        if num_skills > 1:
            skill_rand = random.choice(range(0,num_skills))
        return skill_rand

    def RandomizeStats(self):
        rand_num = random.choice([0,1,2,3])

        if rand_num == 0:
            self.weapon = Weapon("war axe")
            self.aux_weapon = Weapon("none")
            self.skills = [Skill("basic attack"), Skill("sweep")]
            self.health_max = 24
            self.Heal()

        elif rand_num == 1:
            self.weapon = Weapon("dagger")
            self.aux_weapon = Weapon("dagger")
            self.skills = [Skill("basic attack", Skill("backstab"))]
            self.health_max = 12
            self.Heal()

        elif rand_num == 2:
            self.weapon = Weapon("great sword")
            self.aux_weapon = Weapon("none")
            self.skills = [Skill("basic attack"), Skill("bash"), Skill("thrust")]
            self.health_max = 21
            self.Heal()
            
        elif rand_num == 3:
            self.weapon = Weapon("curved sword")
            self.aux_weapon = Weapon("none")
            self.skills = [Skill("basic attack"), Skill("blind spot"), Skill("thrust")]
            self.health_max = 17
            self.Heal()

        
