#imports
from UI.menu import Menu
from PlayerUtilities.player import Player
from Tools.weapons import Weapon
from Tools.skills import Skill
from WorldElements.shop import Shop


# mnT = Menu()
# mnT.SwitchMenu("Main",["Shop","Colosseum","Inventory","Exit Game"])
# mnT.DrawMenu()

# TODO
# DO NOT FORGET
# print(pl.__getattribute__("weapon"))

def startGame():
    mn = Menu()
    player_weapon = Weapon("sword")
    pl_blank_weapon = Weapon("none")
    player_skills = [Skill("basic attack"), Skill("guard")]
    player = Player(player_weapon, pl_blank_weapon,player_skills, 10, 10, ["sword"])
    
    enemy_weapon = Weapon("sword")
    current_enemy = Player(enemy_weapon, pl_blank_weapon,[Skill("basic attack")], 4,4,[])
    
    shop = Shop(player_skills)
    shop_points = 0

    game_loop = True

    while game_loop:
        top_menu = ""
        current_menu = ["Shop","Colosseum","Inventory","Exit Game"]

        mn.SwitchMenu("Main", 0, current_menu)
        mn.DrawMenu()

        u_input = int(input())
        u_input -= 1

        if current_menu.__len__() > u_input and u_input >= 0:
            
        

            if current_menu[u_input] == "Shop":
                top_menu = current_menu[u_input]

                current_menu = ["Weapons", "Skills", "Leave"]
                mn.SwitchMenu(top_menu, 0, current_menu)
                mn.DrawMenu()

                u_input = int(input())
                u_input -=1
                if current_menu.__len__() > u_input and u_input >= 0:

                    if current_menu[u_input] == "Weapons":
                        weapon_menu = u_input + 1
                        
                        current_menu = []

                        for temp_weapon2 in shop.__getattribute__("weapon_list"):
                            current_menu.append(str(temp_weapon2).title())

                        current_menu.append("Leave")
                        
                        while weapon_menu == 1:
                            mn.SwitchMenu(top_menu, weapon_menu, current_menu)
                            mn.DrawMenu()

                            u_input = int(input())
                            u_input -=1
                            if current_menu.__len__() > u_input and u_input >= 0:
                                if current_menu[u_input] != "Leave":
                                    temp_menu = ["Purchase","Cancel", f"You have {shop_points} shop credit(s)"]

                                    #Show weapon stats first, then ask for an auxillary equip
                                    player_weapon.ChangeWeapon(str(current_menu[u_input]).lower())

                                    mn.SwitchMenu(top_menu, weapon_menu, temp_menu, player_weapon)
                                    mn.DrawMenu()

                                    u_input = int(input())
                                    u_input -=1

                                    if temp_menu.__len__() > u_input and u_input >= 0:
                                        
                                        if temp_menu[u_input] == "Purchase":
                                            if shop_points > 0:
                                                player_weapons = player.__getattribute__("all_weapons")
                                                player_weapons.append(player_weapon.__getattribute__("weapon_name"))
                                                player.__setattr__("all_weapons", player_weapons)
                                                
                                                shop_points -= 1
                                                weapon_menu = 0
                                                
                                                print(f"You bought the {player_weapon.__getattribute__("weapon_name")}")
                                            else:
                                                print("You don't have any shop credit right now")

                                        else:
                                            pass
                                    else:
                                        print("Please Select a Valid Option")
                                else:
                                    weapon_menu = 0
                            else:
                                print("Please Select a Valid Option")
                    
                    elif current_menu[u_input] == "Skills":
                        skill_menu = u_input + 1
                        current_menu = []
                        shop.UpdateSkillList(player.__getattribute__("skills"))

                        for skill in shop.__getattribute__("skill_list"):
                            current_menu.append(str(skill).title())
                        current_menu.append("Leave")

                        while skill_menu == 2:
                            mn.SwitchMenu(top_menu, u_input, current_menu)
                            mn.DrawMenu()

                            u_input = int(input())
                            u_input -=1

                            if current_menu.__len__() > u_input and u_input >= 0:
                                if current_menu[u_input] != "Leave":
                                    temp_menu = ["Purchase","Cancel", f"You have {shop_points} shop credit(s)"]

                                    temp_skill = Skill(str(current_menu[u_input]).lower())

                                    mn.SwitchMenu(top_menu, skill_menu, temp_menu, temp_skill)
                                    mn.DrawMenu()

                                    u_input = int(input())
                                    u_input -=1

                                    if temp_menu.__len__() > u_input and u_input >= 0:
                                        
                                        if temp_menu[u_input] == "Purchase":
                                            if shop_points > 0:
                                                temp_list = player.__getattribute__("skills")
                                                temp_list.append(temp_skill)
                                                player.__setattr__("skills", temp_list)
                                                
                                                shop_points -= 1
                                                skill_menu = 0
                                                
                                                print(f"You learned {temp_skill.__getattribute__("skill_name")}")
                                            else:
                                                print("You don't have any shop credit right now")

                                        else:
                                            pass
                                    else:
                                        print("Please Select a Valid Option")
                                else:
                                    skill_menu = 0
                            else:
                                print("Please Select a Valid Option")

                        pass
                    else:
                        pass
                else:
                    print("Please Select a Valid Option")
                pass
            elif current_menu[u_input] == "Colosseum":
                top_menu = current_menu[u_input]
                fight_active = True

                if player.__getattribute__("current_health") > 10:
                    current_enemy.RandomizeStats()

                player_active_skills = []
                enemy_active_skills = []
                enemy_next_attack = ""

                #set up skills for both weapons for both the player and enemy
                for skill in player.__getattribute__("skills"):

                    skill_equipable = skill.__getattribute__("equipable")
                    skill_equipable = str(skill_equipable).split("/")

                    for equipable in skill_equipable:
                        if player.__getattribute__("weapon").__getattribute__("weapon_name").__contains__(equipable):
                            player_active_skills.append([skill,"",0])
                        elif equipable == "all":
                            player_active_skills.append([skill,"",0])
                
                if player.__getattribute__("aux_weapon").__getattribute__("weapon_name") != "none":
                    for skill in player.__getattribute__("skills"):

                        skill_equipable = skill.__getattribute__("equipable")
                        skill_equipable = str(skill_equipable).split("/")

                        for equipable in skill_equipable:
                            if player.__getattribute__("aux_weapon").__getattribute__("weapon_name").__contains__(equipable):
                                player_active_skills.append([skill,"aux",0])
                            elif equipable == "all":
                                player_active_skills.append([skill,"aux",0])

                for skill in current_enemy.__getattribute__("skills"):

                    skill_equipable = skill.__getattribute__("equipable")
                    skill_equipable = str(skill_equipable).split("/")

                    for equipable in skill_equipable:
                        if current_enemy.__getattribute__("weapon").__getattribute__("weapon_name").__contains__(equipable):
                            enemy_active_skills.append([skill,"",0])
                        elif equipable == "all":
                            enemy_active_skills.append([skill,"",0])
                
                if current_enemy.__getattribute__("aux_weapon").__getattribute__("weapon_name") != "none":
                    for skill in current_enemy.__getattribute__("skills"):

                        skill_equipable = skill.__getattribute__("equipable")
                        skill_equipable = str(skill_equipable).split("/")

                        for equipable in skill_equipable:
                            if current_enemy.__getattribute__("aux_weapon").__getattribute__("weapon_name").__contains__(equipable):
                                enemy_active_skills.append([skill,"aux",0])
                            elif equipable == "all":
                                enemy_active_skills.append([skill,"aux",0])
            

                while fight_active:
                    # tick down cooldowns for player
                    i = 0
                    for skill in player_active_skills:
                        if skill[2] != 0:
                            player_active_skills[i][2] -= 1
                        i+=1

                    
                    current_menu = []
                    for skill in player_active_skills:
                        current_menu.append("CD:" + str(skill[2]) + " " + skill[0].__getattribute__("skill_name").title())

                    enemy_turn = True

                    while enemy_turn:
                        enemy_next_attack_id = current_enemy.RandomAttack(enemy_active_skills)
                        if enemy_active_skills[enemy_next_attack_id][2] == 0:
                            enemy_next_attack = enemy_active_skills[enemy_next_attack_id][0].__getattribute__("skill_name")
                            enemy_turn = False

                    i = 0
                    for skill in enemy_active_skills:
                        if skill[2] != 0:
                            enemy_active_skills[i][2] -= 1
                        i+=1

                    enemy_health = current_enemy.__getattribute__("current_health")
                    player_health = player.__getattribute__("current_health")

            
                    mn.SwitchMenu(top_menu, enemy_next_attack, current_menu, current_enemy, player)
                    mn.DrawMenu()

                    player_turn = True

                    while player_turn:
                        u_input = int(input())
                        u_input -= 1

                        player_damage = 0
                        player_attack = player_active_skills[u_input]
                    
                        
                        if player_attack[2] == 0:
                            # setting cooldown here for the used skill
                            player_active_skills[u_input][2] += player_active_skills[u_input][0].__getattribute__("cooldown")

                            if player_attack[1] != "aux":
                                player_damage = player.__getattribute__("weapon").__getattribute__("base_damage") * player_attack[0].__getattribute__("multiplier")
                            else:
                                player_damage = player.__getattribute__("aux_weapon").__getattribute__("base_damage") * player_attack[0].__getattribute__("multiplier")

                            enemy_health -= player_damage
                            print(f"You hit your opponent for {str(player_damage)} damage!")
                            current_enemy.__setattr__("current_health", enemy_health)

                            enemy_damage = 0
                            enemy_next_attack = enemy_active_skills[enemy_next_attack_id]

                            if enemy_health > 0:

                                if enemy_next_attack[1] != "aux":
                                    enemy_damage = player.__getattribute__("weapon").__getattribute__("base_damage") * enemy_next_attack[0].__getattribute__("multiplier")
                                else:
                                    enemy_damage = player.__getattribute__("aux_weapon").__getattribute__("base_damage") * enemy_next_attack[0].__getattribute__("multiplier")

                                if player_attack[0].__getattribute__("skill_name") == "guard" or player_attack[0].__getattribute__("skill_name") == "block":
                                    enemy_damage = 0
                                    print("You defended your opponent's attack!")
                                
                                player_health -= enemy_damage
                                print(f"Your opponent hit you for {str(enemy_damage)} damage!")
                                player.__setattr__("current_health", player_health)

                                enemy_active_skills[enemy_next_attack_id][2] += enemy_active_skills[enemy_next_attack_id][0].__getattribute__("cooldown")
                                player_turn = False

                                if player_health <= 0:
                                    fight_active = False
                                    game_loop = False

                                    print("You have fallen in glorious combat at the Colosseum!")
                                    print("It is a shame, but you put on quite the good show")
                                    print("")

                            else:
                                player_turn = False
                                fight_active = False
                                player.ImproveHealth()
                                player.Heal()
                                shop_points += 3
                                print("")
                                print("Hurrah! The crowd cheers for your victory!")
                                print("")
                                print("You have 3 more shop credits.")
                                print("")
                                print("You've rested after the fight, healing your hitpoints and gaining 4 more maximum health.")
                        else:
                            print(f"That skill is still on cooldown for {str(player_attack[2])} more turns")
                        
                        

                # Colosseum Ends here
            elif current_menu[u_input] == "Inventory":
                top_menu = current_menu[u_input]

                current_menu = ["Weapons", "Skills", "Leave"]
                mn.SwitchMenu(top_menu, 0, current_menu)
                mn.DrawMenu()

                u_input = int(input())
                u_input -=1
                if current_menu.__len__() > u_input and u_input >= 0:

                    if current_menu[u_input] == "Weapons":
                        weapon_menu = u_input + 1
                        
                        current_menu = []

                        for temp_weapon2 in player.__getattribute__("all_weapons"):
                            current_menu.append(str(temp_weapon2).title())

                        current_menu.append("Leave")
                        
                        while weapon_menu == 1:
                            mn.SwitchMenu(top_menu, weapon_menu, current_menu)
                            mn.DrawMenu()

                            u_input = int(input())
                            u_input -=1
                            if current_menu.__len__() > u_input and u_input >= 0:
                                if current_menu[u_input] != "Leave":
                                    temp_menu = ["Equip Main","Equip Off-hand","Cancel"]

                                    #Show weapon stats first, then ask for an auxillary equip
                                    player_weapon.ChangeWeapon(str(current_menu[u_input]).lower())

                                    mn.SwitchMenu(top_menu, weapon_menu, temp_menu, player_weapon)
                                    mn.DrawMenu()

                                    u_input = int(input())
                                    u_input -=1

                                    if temp_menu.__len__() > u_input and u_input >= 0:
                                        
                                        if temp_menu[u_input] == "Equip Main":
                                            player.__setattr__("weapon", player_weapon)
                                            
                                            weapon_menu = 0
                                            
                                            print(f"You equipped your {player_weapon.__getattribute__("weapon_name")}")

                                        elif temp_menu[u_input] == "Equip Off-hand":
                                            if player_weapon.__getattribute__("auxillary"):
                                                if str(player.__getattribute__("weapon_name")).__contains__("great") != True:
                                                    player.__setattr__("aux_weapon", player_weapon)

                                                    weapon_menu = 0

                                                    print(f"You equipped your {player_weapon.__getattribute__("weapon_name")}")
                                                else:
                                                    print("You have no free hands, you're holding a great weapon.")
                                            else:
                                                print("You can't equip that weapon in your offhand.")

                                        else:
                                            pass
                                    else:
                                        print("Please Select a Valid Option")
                                else:
                                    weapon_menu = 0
                            else:
                                print("Please Select a Valid Option")
                    
                    elif current_menu[u_input] == "Skills":
                        skill_menu = u_input + 1
                        current_menu = []
                        player_skill_list = player.__getattribute__("skills")

                        for skill in player_skill_list:
                            current_menu.append(str(skill.__getattribute__("skill_name")).title())
                        current_menu.append("Leave")

                        mn.SwitchMenu(top_menu, u_input, current_menu)

                        while skill_menu == 2:
                            mn.DrawMenu()

                            u_input = int(input())
                            u_input -=1

                            if current_menu.__len__() > u_input and u_input >= 0:
                                if current_menu[u_input] == "Leave":
                                    skill_menu = 0
                                else:
                                    mn.SwitchMenu(top_menu, skill_menu, current_menu, player_skill_list[u_input])
                            else:
                                print("Please Select a Valid Option")

                        pass
                    else:
                        pass
                else:
                    print("Please Select a Valid Option")
                
            elif current_menu[u_input] == "Exit Game":
                game_loop = False
        else:
            print("Please Select a Valid Option")


    print("Farewell Challenger, you are welcome back anytime!")
    pass



if __name__ == '__main__':
    startGame()