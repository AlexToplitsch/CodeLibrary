class Player:
    def __init__(self, name: str, symbol: str):
        self.__name = name
        self.__symbol = symbol
    
    def getSymbol(self):
        return self.__symbol


    def getName(self):
        return self.__name