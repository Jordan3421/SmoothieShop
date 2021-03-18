from src.Display.Input import Input
from src.DataSource.WriteToFile import WriteToFile
from src.DataSource.DataSourceConstants import *

class InputConsole(Input):

    writeToFile = True
    userInputWriteToFile = WriteToFile(USERACTION_FOLDER,INPUT_LOG)

    def getInputString(self, request):
        userInput = input(request)
        if self.writeToFile:
            self.userInputWriteToFile.writeToFile(userInput)
        return userInput

    def getInputInt(self, request):
        response = self.getInputString(request)
        while not str(response).isnumeric():
            response = self.getInputString("Please enter an integer")
        return int(response)
