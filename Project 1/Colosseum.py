#imports
from UI.menu import Menu
from PlayerUtilities.player import Player
from Tools.weapons import Weapon
from Tools.skills import Skill
from WorldElements.shop import Shop


# mnT = Menu()
# mnT.SwitchMenu("Main",["Shop","Colosseum","Inventory","Exit Game"])
# mnT.DrawMenu()

# DO NOT FORGET
# pl = Player("sword","",[],0,0,[])
# print(pl.__getattribute__("weapon"))

class Main():
    def __init__(self) -> None:
        self.startGame()
        pass

    def startGame():
        mn = Menu()
        player_weapon = Weapon("sword")
        pl_blank_weapon = Weapon("none")
        player = Player(player_weapon, pl_blank_weapon,[Skill("basic attack"), Skill("guard")], 10, 10, [])
        
        enemy_weapon = Weapon("sword")
        current_enemy = Player(enemy_weapon, pl_blank_weapon,[Skill("basic attack")], 4,4,[])
        
        shop = Shop()

        game_loop = True

        while game_loop:
            fight_active = False
            #move him to fight logic when you get there

            top_menu = ""
            current_menu = ["Shop","Colosseum","Inventory","Exit Game"]

            mn.SwitchMenu("Main", 0, current_menu)
            mn.DrawMenu()

            if current_menu.__len__() < u_input and u_input >= 0:
                u_input = input()
            else:
                print("Please Select a Valid Option")

            if current_menu[u_input] == "Shop":
                pass
            elif current_menu[u_input] == "Colosseum":
                pass
            elif current_menu[u_input] == "Inventory":
                top_menu = current_menu[u_input]

                current_menu = ["Leave", "Weapons", "Skills"]
                mn.SwitchMenu(top_menu, 0, current_menu)
                mn.DrawMenu()

                if current_menu.__len__() < u_input and u_input >= 0:
                    u_input = input()
                else:
                    print("Please Select a Valid Option")

                if current_menu[u_input] == "Weapons":
                    weapon_menu = True
                    temp_weapon = player.__getattribute__("weapon")
                    current_menu = [str(Weapon(temp_weapon).__getattribute__("weapon_name")).title()]

                    for temp_weapon2 in player.__getattribute__("other_weapons"):
                        current_menu.append(str(temp_weapon2).title())

                    
                    
                    while weapon_menu:
                        mn.SwitchMenu(top_menu, u_input, current_menu)
                        mn.DrawMenu()

                        if current_menu.__len__() < u_input and u_input >= 0:
                            u_input = input()
                            
                        else:
                            print("Please Select a Valid Option")
                        #Show weapon stats first, then ask for an auxillary equip
                        player_weapon.ChangeWeapon(current_menu[u_input])

                        print(f"You equipped your {current_menu[u_input]}")
                    
                elif current_menu[u_input] == "Skills":
                    skill_menu = True
                    current_menu = []
                    player_skill_list = player.__getattribute__("skills")

                    for skill in player_skill_list:
                        current_menu.append(str(Skill(skill).__getattribute__("skill_name")).title())
                    current_menu.append("Leave")

                    mn.SwitchMenu(top_menu, u_input, current_menu)

                    while skill_menu:
                        mn.DrawMenu()

                        u_input = input()

                        if current_menu.__len__() < u_input and u_input >= 0:
                            if current_menu[u_input] == "Leave":
                                skill_menu = False
                            else:
                                mn.SkillMenuSwitch(player_skill_list[u_input])
                        else:
                            print("Please Select a Valid Option")

                    pass
                else:
                    pass
                
            elif current_menu[u_input] == "Exit Game":
                game_loop = False


        print("Farewell Challenger, you are welcome back anytime!")
        pass
