import data
from choice import Player, Choice
from gui import CrwrGUI

def init_list(length, texts, mags, options, unless):
    choices = []
    for i in range(length):
        choices.append(Choice(i, texts[i], mags[i], options[i], unless[i]))
    
    return choices

def main():
    player = Player()
    gui = CrwrGUI()
    game_cont = True
    pop_size = 1000000000
    choices = init_list(6, data.texts, data.mags, data.options, data.unless)
    curr_choice = choices[0]

    while game_cont:
        if pop_size < 1:
            game_cont = False
        #other conditions for game to end early
        click = gui.getWin().getMouse()
        for button in gui.get_active_buttons():
            c = button.clicked(click)
            if c:
                gui.close_curr()
                if type(c) == int and gui.next_scene == 'P':
                    curr_choice = choices[choices[c].get_choice(0)]
                if gui.next_scene == 'P':
                    gui.open_prompt(curr_choice.get_text())
                elif gui.next_scene == 'C':
                    gui.open_choices(choices, curr_choice.get_choices())
                gui.draw_curr(curr_choice.unless)
                c = 0
                break

main()


        
