from src.DataSource.ReadMenu import ReadMenu
from src.Display.InputConsole import InputConsole


class CreateCustomSmoothie:

    def __init__(self):
        readIngredientsMenu = ReadMenu()
        self.ingredientsMenu = readIngredientsMenu.readMenu('Ingredients.csv')

        self.ingredientsList = []
        for ingredient in self.ingredientsMenu:
            self.ingredientsList.append(f"{ingredient[0]} ({self.ingredientsMenu.index(ingredient)+1})")

        self.customIngredients = []

    def getUserIngredientChoice(self):

        inputConsole = InputConsole()
        userChoice = inputConsole.getInputInt("Enter your desired ingredient's corresponding number to add it to your smoothie!")

        return userChoice


    def addUserIngredientChoiceToSmoothie(self):
        self.userIngredientChoice = self.getUserIngredientChoice()
        self.customIngredients.append(self.ingredientsList[self.userIngredientChoice-1])
        print('you added ', self.customIngredients)



e = CreateCustomSmoothie()
print(e.ingredientsList)
e.addUserIngredientChoiceToSmoothie()


