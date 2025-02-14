import data
from choice import Player, Choice
from gui import CrwrGUI

def init_list(length, texts, mags, options):
    choices = []
    for i in range(length):
        choices.append(Choice(i, texts[i], mags[i], options[i]))
    
    return choices

def run_choice(choice):
    print("\n")
    print(choices[tag].get_text())
    #print option taglines??

def user_choice():
    user = False
    while not user:
        user_choice = input("Please type the number corresponding with the option you'd like to select")
        if type(user_choice) != int:
            print("Please type a valid integer")
        else if user_choice >
    #fill out user choice function


def main():
    player = Player()
    gui = CrwrGUI()
    game_cont = True
    pop_size = 1000000000
    choices = init_list(5, data.texts, data.mags, data.options)
    curr_choice = 0

    while game_cont:
        if pop_size < 1:
            game_cont = False
        #other conditions for game to end early
        click = gui.getWin().getMouse()
        if gui.begin_button.clicked(click):
            gui.close_curr()
            if input("Type kill to kill: ") == "kill":
                gui.killWin()
            gui.prompt_scene()
        elif gui.next_button.clicked(click):
            gui.close_curr()
            gui.choice_scene()
        else:
            for choice in gui.curr_choices():
                if choice.button.clicked(click):
                    gui.close_curr()
                    #progress to next prompt scene

main()


        
