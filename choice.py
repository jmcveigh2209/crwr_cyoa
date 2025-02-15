import math

# Player class: No parameters
# potential future parameters: asab, intelligence, empathy, physical fitness/ability, sexuality
class Player:
    def __init__(self):
        self.worst_decision = 0
        self.people_killed = 0
        self.humanity_meter = 8
        #insert more attributes if decided on parameters; certain choices could impact parameter values??

    def murder(self, num):
        self.people_killed += num
        if num > 50:
            self.humanity_meter -= 2
        else:
            self.humanity_meter -= 1
        if self.humanity_meter < 0:
            self.humanity_meter = 0

    def do_good(self):
        if self.humanity_meter < 10:
            self.humanity_meter += 1
        return self.humanity_meter

    def bad_choices(self, tag):
        self.worst_decision = tag

    def get_kills(self):
        return self.people_killed

    def get_stats(self):
        return self.worst_decision, self.people_killed


"""
Choice class parameters:
 - tag (int): number choice is referred to by; index in choice list
 - text (str): text displayed when choice is presented
 - magnitude (int): scale of 1-5 how 'bad' having made this choice is for your karma
 - options (list(tag)): choices this option presents; this leaf's children in the tree
"""   
class Choice:
    def __init__(self, tag, text, magnitude, choices, unless):
        self.tag = tag
        self.text = text
        self.mag = magnitude
        self.child_choices = choices #in numerical order
        self.unless = unless

    def get_tag(self):
        return self.tag

    def get_mag(self):
        return self.mag

    def get_text(self):
        return self.text

    def get_choices(self):
        return self.child_choices

    def get_choice(self, num):
        if num <= len(self.child_choices):
            return self.child_choices[num]
        else:
            print("Error: Invalid Choice")

