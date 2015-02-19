""" 
Card class for the DURAK game.
"""
#List of colors
colors = ['Spades', 'Hearths', 'Diamonds', 'Clubs']

#Figures to values map
figures = {'6'      : 6,
           '7'      : 7,
           '8'      : 8,
           '9'      : 9,
           '10'     : 10,
           'Jack'   : 11,
           'Queen'  : 12,
           'King'   : 13,
           'Ace'    : 14,}
    
class Card(object):
    __is_trump  = False
    __color     = 'Wrong Color'
    __figure    = 'Wrong Figure'
    __value     = -1
    
    # Figure should be figures key
    def __init__(self, color, figure):
        if color in colors:
            self.__color = color
        else: 
            print "Wrong color"
        if figure in figures.keys():
            self.__figure = figure
            self.__value = figures[figure]
        else:
            print "wrong figure"
        
    def __repr__(self):
        return "#### %s of %s" %(self.__figure, self.__color)
    
    def get_value(self):
        return self.__value
    
    def set_trump(self, color):
        if self.__color == color:
            self.__is_trump = True
            self.__value += 100   
       
       

