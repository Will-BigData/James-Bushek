import pandas as pd
import re
import mysql.connector

class Menu():
    def __init__(self, menu=["-------------------------------------------",[],[],[],"-------------------------------------------"],
                answers = ['Bragge\'s','Colosseum','Inventory','Weapons','Skills','Leave']) -> None:
        self.menu = menu
        self.answers = answers

    def __DrawMenu__():
        #just iterate through the menu listlist
        #and print to console
        pass

    def SwitchMenu(self,scene):
        #read the prompts file
        cnx = mysql.connector.connect(user='root',password='tSn3U-vDA>4^!),E',host='localhost',database='colosseum')
        cursor = cnx.cursor()
        cursor.execute("USE colosseum")

        if scene == "main":
            cursor.execute("SELECT Prompt FROM Prompts WHERE Scene = 'Main'")
            # filter the prompts for the main menu ones
            prompts_main = cursor.fetchall()
            self.SetMainMenu(prompts_main) # pass in the prompts
            # copy this for the others too
        elif scene == "fight":

            self.SetFightMenu()
        elif scene == "shop":

            self.SetShopMenu()
        elif scene == "inventory":

            self.SetInventoryMenu()
        else:
            print('HOW has something gone this wrong')
            pass

        self.__DrawMenu__()

    def SetMainMenu(self,prompts):
        #pick one of the prompts
        prompt_main = self.CleanUpPrompt(prompts[0])
        self.menu[1] = prompt_main
        print(prompt_main)

    def SetFightMenu():
        pass

    def SetShopMenu():
        pass

    def SetInventoryMenu():
        pass


    def CleanUpPrompt(self, prompt):
        # cleaned = re.sub("[\\]", '', str(prompt))
        # cleaned2 = cleaned[2:-3]
        cleaned2 = str(prompt)[2:-3]
        return cleaned2
        #pass