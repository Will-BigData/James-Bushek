import mysql.connector
from Tools.weapons import Weapon
from Tools.skills import Skill

# TODO: set Fight, Shop, and Inventory methods
# a turn switch Fight menu method

class Menu():
    def __init__(self, menu=["________________________________________________________", "--------------------------------------------------------",[],[""],[],"--------------------------------------------------------"]) -> None:
        self.menu = menu

    def DrawMenu(self):
        #just iterate through the menu listlist
        #and print to console

        for item in self.menu:
            if type(item) == list:
                for sub_item in item:
                    print(sub_item)
            else:
                print(item)
        pass

    def SwitchMenu(self, scene, menu_index, options, extra="", extra2=""):
        #read the prompts file
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")

        if scene == "Main":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Main'")
            # filter the prompts for the main menu ones

            prompts_main = cursor.fetchall()

            self.SetMainMenu(prompts_main, options) # pass in the prompts
            # copy this for the others too

        elif scene == "Colosseum":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Fight'")

            prompts_fight = cursor.fetchall()

            self.SetFightMenu(menu_index, options, extra, extra2)

        elif scene == "Shop":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Shop'")

            prompts_shop = cursor.fetchall()

            self.SetShopMenu(menu_index, options, extra)

        elif scene == "Inventory":
            self.SetInventoryMenu(menu_index, options, extra)

        else:
            print('HOW has something gone this wrong')
            pass
        
        cursor.close()
        cnx.close()


    def SetMainMenu(self, prompts, options):
        #pick one of the prompts
        prompt_main = self.__CleanUpPrompt__(prompts[0])

        self.menu[2] = []
        self.menu[2].append(prompt_main)

        self.menu[4] = self.__FormatOptions__(options)

    def SetFightMenu(self, enemy_next_attack, options, current_enemy, player):
        self.menu[2] = []

        self.menu[4] = self.__FormatOptions__(options)

        health1 = current_enemy.__getattribute__("current_health")
        health2 = player.__getattribute__("current_health")

        self.menu[2].append(f"Your opponent wields a {current_enemy.__getattribute__("weapon").__getattribute__("weapon_name").title()}")
        self.menu[2].append(f"They're preparing to use {enemy_next_attack}")
        self.menu[2].append(f"Enemy HP: {str(health1)}")
        self.menu[2].append("")
        self.menu[2].append(f"Your HP: {str(health2)}")

    def SetShopMenu(self, menu_index, options, current_item):
        self.menu[2] = []
        self.menu[4] = self.__FormatOptions__(options)

        if menu_index == 1:
            self.__SetWeapon__(current_item)
        elif menu_index == 2:
            self.__SetSkill__(current_item)

    def SetInventoryMenu(self, menu_index, options, player_item):
        self.menu[2] = []
        self.menu[4] = self.__FormatOptions__(options)

        if menu_index == 1:
            self.__SetWeapon__(player_item)
        elif menu_index == 2:
            self.__SetSkill__(player_item)

    def __SetWeapon__(self, player_item):
        if type(player_item) == Weapon:
                weapon_name = str(player_item.__getattribute__("weapon_name")).title() + ":"
                base_damage = player_item.__getattribute__("base_damage")
                auxillary = player_item.__getattribute__("auxillary")
                self.menu[2] = [weapon_name, f"Base Damage: {base_damage}", f"Offhand Weapon: {auxillary}"]
            # else:
            #     print("it didn't work :(")

    def __SetSkill__(self, player_item):
        if type(player_item) == Skill:
                skill_name = str(player_item.__getattribute__("skill_name")).title() + ":"
                equipable = player_item.__getattribute__("equipable")
                multiplier = player_item.__getattribute__("multiplier")
                cooldown = player_item.__getattribute__("cooldown") - 1
                self.menu[2] = [skill_name,f"Usable With: {equipable}",f"Damage Mulitplier: {multiplier}",f"Cooldown: {cooldown} Turns"]
            # else:
            #     print("it didn't work :(")


    def __CleanUpPrompt__(self, prompt):
        # cleaned = re.sub("[\\]", '', str(prompt))
        # cleaned2 = cleaned[2:-3]

        cleaned2 = str(prompt)[2:-3]
        return cleaned2
    
        #pass

    def __FormatOptions__(self, options):
        i = 1
        all_options = []
        current_row = ""

        for opt in options:
            opt += f" [{i}] | "
            
            if current_row == "":
                opt = "| " + opt
            
            current_row += opt
            if i%3 == 0:
                all_options.append(current_row)
                current_row = ""
            
            i+=1
        all_options.append(current_row)
        return all_options
