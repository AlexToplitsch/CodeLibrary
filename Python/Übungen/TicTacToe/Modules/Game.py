from Modules.Player import Player as p
from Modules.Board import Board as b

class Game:

    def __init__(self):
        self.__player1 = p("Player1", "X")
        self.__player2 = p("Player2", "O")
        self.__board = b().getInstance()

    def run(self):
        run = True
        player = self.__player1
        while run == True:
            
