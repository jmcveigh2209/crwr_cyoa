import math

# Player class: No parameters
# potential future parameters: asab, intelligence, empathy, physical fitness/ability, sexuality
class Player:
    def __init__(self):
        self.worst_decision = 0
        self.people_killed = 0
        #insert more attributes if decided on parameters; certain choices could impact parameter values??

    def murder(self, num):
        self.people_killed += num

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
    def __init__(self, tag, text, magnitude, options):
        self.tag = tag
        self.text = text
        self.mag = magnitude
        self.options = options #in numerical order

    def get_tag(self):
        return self.tag

    def get_mag(self):
        return self.mag

    def get_text(self):
        return self.text

    def get_options(self):
        return self.options

    def get_option(self, num):
        return self.options[num] #num can't be larger than max index of options

