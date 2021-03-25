import csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class Menu:
    def smoothieMenu(self, menuName):
        readCSVFile = ReadCSVFile()
        smoothieMenu = readCSVFile.getFileData(entitiesFolder, menuName + ".csv")
        return smoothieMenu
