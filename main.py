import data
from choice import Player, Choice

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
    game_cont = True
    pop_size = 8204160114
    choices = init_list(5, data.texts, data.mags, data.options)
    curr_choice = 0

    while game_cont:
        if pop_size < 1:
            game_cont = False
        #other conditions for game to end early
        run_choice(choices[curr_choice])
        curr_choice = user_choice


        
