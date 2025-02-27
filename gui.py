#This file contains CYOA GUI Class which runs the GUI of the program
"""
Tasks for Group Meeting
- Name project label
"""

from graphics import *
from button import Button
from choice import Choice
import math

class CrwrGUI:
    def __init__(self):
        self.win = GraphWin("DAJ", 1920, 1080)
        self.win.setCoords(0,0,1919, 1079)
        self.center_x = 959
        self.win.setBackground("black")
        self.active_comps = []
        self.active_buttons = []
        self.open_opening()
        self.draw_curr()
        self.next_scene = 'P'

    def open_opening(self):
        line1 = Text(Point(self.center_x, 365), "Welcome to")
        setTextSettings(line1, 36, 'bold italic')
        line2 = Text(Point(self.center_x, 290), "The Second Genesis")
        setTextSettings(line2, 40, 'bold italic')
        self.begin_button = Button(self.getWin(), Point(self.center_x, 130), 65, 30, "Begin", "white", "white")
        self.begin_button.setLabelColor('white')
        self.begin_button.getLabel().setFace("courier")
        self.active_buttons.append(self.begin_button)
        self.active_comps.extend([line1, line2, self.begin_button])

    def open_prompt(self, text):
        line1 = Text(Point(self.center_x, 365), "What is your decision?")
        setTextSettings(line1, 16)
        line2 = Text(Point(self.center_x, 300), text)
        setTextSettings(line2, 13)
        self.next_button = Button(self.getWin(), Point(self.center_x, 130), 65, 30, "Next ->", 'white', 'white')
        self.next_button.setLabelColor('white')
        self.next_button.getLabel().setFace("courier")
        self.active_buttons.append(self.next_button)
        self.active_comps.extend([line1, line2, self.next_button])
        self.next_scene = 'C'

    def open_choices(self, choices, curr_choices, unless=[]):
        line1 = Text(Point(self.center_x, 405), "What is your decision?")
        setTextSettings(line1, 16)
        self.active_comps.append(line1)
        i = 0
        j = 0
        width = 300
        height = 150
        for curr in curr_choices:
            choice_gui = ChoiceGUI(choices[curr], 25+i, 25+j, width, height)
            self.active_comps.append(choice_gui)
            self.active_buttons.append(choice_gui)
            i += width + 25
            if i % 2 == 0:
                i = 0
                j += height + 25
        self.activate_buttons
        self.next_scene = 'P'

    def draw_curr(self, unless=[]):
        'draws current scene'
        for obj in self.active_comps:
            obj.draw(self.win)
        self.activate_buttons(unless)

    def get_active_buttons(self):
        return self.active_buttons

    def activate_buttons(self, unless=[]):
        for i in range(len(self.active_buttons)):
            if i not in unless:
                self.active_buttons[i].activate()

    def deactivate_buttons(self):
        while self.active_buttons:
            self.active_buttons[0].deactivate()
            self.active_buttons.pop(0)
    
    def close_curr(self):
        'close current scene'
        self.deactivate_buttons()
        while self.active_comps:
            self.active_comps[0].undraw()
            self.active_comps.pop(0)
        
    def getWin(self):
        return self.win

    def killWin(self):
        self.close_curr()
        self.win.close()

class ChoiceGUI:
    def __init__(self, choice: Choice, xll, yll, width, height):
        self.choice = choice
        self.xll = xll
        self.yll = yll
        self.xur = self.xll + width
        self.yur = self.yll + height
        self.box = Rectangle(Point(xll, yll), Point(self.xur, self.yur))
        self.setOutline('white')
        height_offset = findTextHeight(choice.get_text(), 13) + 10
        self.text = Text(Point(xll+(width/2), self.yur-height_offset), choice.get_text())
        setTextSettings(self.text, 13)
        self.active = False

    def setOutline(self, color):
        self.box.setOutline(color)

    def activate(self):
        self.active = True
        return self.active
    
    def deactivate(self):
        self.active = False
        return self.active

    def clicked(self, pt):
        'checks to see if choice was clicked'
        if self.active and self.xll <= pt.getX() <= self.xur and self.yll <= pt.getY() <= self.yur:
            return self.choice.get_tag()
        return False

    def draw(self, win):
        self.box.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.box.undraw()
        self.text.undraw()

def setTextSettings(variable, size=20, style='bold', color='white', face='courier'):
        variable.setSize(size)
        variable.setStyle(style)
        variable.setTextColor(color)
        variable.setFace(face)

def findTextHeight(text, size):
    num = 0
    for char in text:
        if char == '\n':
            num += 1
    return math.ceil((num/2) * (size * (4/3)))
