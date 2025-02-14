#This file contains the Button class for GUI purposes

from graphics import *

# create Button class
class Button:
    def __init__(self, win, center, width, height, label, txtColor = 'black', outlineColor='black'):
        'sets instance variables'
        self.window = win
        self.select = False
        self.center = center
        self.centerX = center.getX()
        self.centerY = center.getY()
        self.width = width
        self.height = height
        self.text = label
        self.textColor = txtColor
        self.outlineColor = outlineColor
        'Calculate button coordinates'
        self.xll = self.centerX - (self.width/2)
        self.yll = self.centerY - (self.height/2)
        self.xur = self.centerX + (self.width/2)
        self.yur = self.centerY + (self.height/2)
        'Create button'
        self.button = Rectangle(Point(self.xll, self.yll), Point(self.xur, self.yur))
        'Set label and outline of button'
        self.label = Text(self.center, self.text)
        self.button.setOutline(self.outlineColor)
        self.button.draw(self.window)
        self.label.draw(self.window)
        self.deactivate()

    def getWindow(self):
        'returns the window the class is being drawn in'
        return self.getWindow
    
    def getCenter(self):
        'returns the center point'
        return self.center
    
    def getWidth(self):
        'returns the width value'
        return self.width
    
    def getHeight(self):
        'returns the height value'
        return self.height
    
    def getLabel(self):
        'returns the current label value'
        return self.label

    def setWidth(self, newWidth):
        'a little confusion but this sets the width of the outline not the width of the button'
        self.button.setWidth(newWidth)
    
    def clicked(self, pt):
        'checks to see if the button was clicked'
        if self.active and self.xll <= pt.getX() <= self.xur and self.yll <= pt.getY() <= self.yur:
            'if button clicked, yes click and deactive button'
            self.click = True
            return self.click
        else:
            'otherwise not click'
            self.click = False
            return self.click

    def activate(self):
        'make button clickable'
        #self.label.setFill('white')
        self.active = True

    def setLabel(self, newText):
        'change label to newText'
        self.label.setText(newText)

    def setLabelColor(self, newColor):
        'changes color of label text'
        self.label.setTextColor(newColor)

    def setLabelStyle(self, newStyle):
        'changes style of label text'
        self.label.setStyle(newStyle)

    def setLabelSize(self, size):
        'changes size of label text'
        self.label.setSize(size)

    def setColor(self, newColor):
        'change fill color of button'
        self.button.setFill(newColor)

    def setOutline(self, newOutline):
        'change outline color of button'
        self.button.setOutline(newOutline)

    def deactivate(self):
        'makes button unclickable'
        self.active = False

    def holdSelect(self, newColor, newWidth):
        'changes color and border of button'
        self.setOutline(newColor)
        self.setWidth(newWidth)
        self.Select = True

    def deselect(self, ogWidth=1):
        'returns button to original color and border size'
        self.setOutline(self.outlineColor)
        self.setWidth(ogWidth)
        self.Select = False

    def undraw(self):
        'undraws button'
        self.label.undraw()
        self.button.undraw()