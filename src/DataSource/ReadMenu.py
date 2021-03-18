from src.DataSource.ReadCSVFile import *

class ReadMenu():


    def readMenu(self, menuFile):

        readCSVFile = ReadCSVFile()


        menu = readCSVFile.getFileData('Fruits/', menuFile)

        return menu


