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

    def SwitchMenu(self, scene, menu_index, options):
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

        elif scene == "Fight":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Fight'")

            prompts_fight = cursor.fetchall()

            self.SetFightMenu()

        elif scene == "Shop":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Fight'")

            prompts_shop = cursor.fetchall()

            self.SetShopMenu()

        elif scene == "Inventory":

            self.SetInventoryMenu(menu_index, options)

        else:
            print('HOW has something gone this wrong')
            pass
        
        cursor.close()
        cnx.close()


    def SetMainMenu(self, prompts, options):
        #pick one of the prompts
        prompt_main = self.__CleanUpPrompt__(prompts[0])

        self.menu[2].append(prompt_main)

        self.menu[4] = self.__FormatOptions__(options)

    def SetFightMenu():
        pass

    def SetShopMenu():
        pass

    def SetInventoryMenu(self, menu_index, options):
        self.menu[4] = self.__FormatOptions__(options)
        pass

    def SkillMenuSwitch(self, skill:Skill):
        skill_name = str(skill.__getattribute__("skill_name")).title() + ":"
        equipable = skill.__getattribute__("equipable")
        multiplier = skill.__getattribute__("multiplier")
        cooldown = skill.__getattribute__("cooldown")
        self.menu[2] = [skill_name,f"Usable On: {equipable}",f"Damage Mulitplier: {multiplier}",f"Cooldown: {cooldown}"]



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
