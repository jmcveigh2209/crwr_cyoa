#This file contains CYOA GUI Class which runs the GUI of the program
"""
Tasks for Group Meeting
- Name project label
"""

from graphics import *
from button import Button

class CrwrGUI:
    def __init__(self):
        self.win = GraphWin("DAJ", 700, 500)
        self.win.setCoords(0,0,699,499)
        self.win.setBackground("black")
        self.active_comps = []
        self.open_opening()

    def open_opening(self):
        line1 = Text(Point(349, 365), "Welcome to")
        line1.setSize(36)
        line1.setStyle('bold italic')
        line1.setTextColor('white')
        line1.setFace("courier")
        line1.draw(self.getWin())
        line2 = Text(Point(349, 290), "The Second Genesis")
        line2.setSize(40)
        line2.setStyle('bold italic')
        line2.setTextColor('white')
        line2.setFace("courier")
        line2.draw(self.getWin())
        self.begin_button = Button(self.getWin(), Point(349, 130), 65, 30, "Begin", "white", "white")
        self.begin_button.setLabelColor('white')
        self.begin_button.getLabel().setFace("courier")
        self.begin_button.activate()
        self.active_comps.extend([line1, line2, self.begin_button])

    #def prompt(self, text):

    def close_curr(self):
        'close current scene'
        for obj in self.active_comps:
            obj.undraw()
        
    def getWin(self):
        return self.win

    def killWin(self):
        self.close_curr()
        self.win.close()

