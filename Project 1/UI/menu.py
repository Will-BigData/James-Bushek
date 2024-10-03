import pandas as pd


class Menu():
    def __init__(self, menu=[[],[],[],[],[]], menu_max=0) -> None:
        self.menu = menu
        self.menu_max = menu_max

    def DrawMenu():
        #just iterate through the menu listlist
        #and print to console
        pass

    def SwitchMenu(self,scene) -> None:
        #read the prompts file
        prompts_all = pd.read_csv('GameData/textprompts.csv')
        if scene == "main":
            prompts_main_data = prompts_all.loc[0]
            # filter the prompts for the main menu ones
            prompts_main = [str(prompts_main_data["Prompt"])]
            self.SetMainMenu(prompts_main) # pass in the prompts
            #copy this for the others too
        elif scene == "fight":
            self.SetFightMenu()
        elif scene == "shop":
            self.SetShopMenu()
        else:
            pass

    def SetMainMenu(self,prompts):
        #pick one of the prompts
        prompt_main = prompts[0]
        
        #seperate the string based on the max length of the menu
        pass

    def SetFightMenu():
        pass

    def SetShopMenu():
        pass
