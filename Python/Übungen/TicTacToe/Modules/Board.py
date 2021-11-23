from Modules.Field import Field

class Board:
    __instance = None

    def __init__(self):
        if Board.__instance != None:
            raise Exception("Cannot make an Instance of Singleton class!")
        else:
            self.__fields = []
            self.createFields()
            
    @staticmethod
    def getInstance():
        if Board.__instance == None:
            Board.__instance = Board()
        return Board.__instance

    def createFields(self):
        for i in range(9):
            self.__fields.append(Field(""))

    def pickField(self, symbol:str, fieldNumber:int):
        self.__fields[fieldNumber].setSymbol(symbol)
