class Book:

    def __init__(self):
        self.recipe = {}
        self.list = []

    def add(self, name, ingredients, meal, prep_time):
        self.recipe[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}
        self.list.append(name)

    def remove(self, name):
        self.recipe.pop(name)
        self.list.remove(name)

    def display_recipe(self, name):
        print("Recipe for {}:\n".format(name))
        print("Ingredients list: {}".format(self.recipe[name]['ingredients']))
        print("To be eaten for {}".format(self.recipe[name]['meal']))
        print("Takes {} minutes of cooking".format(self.recipe[name]['prep_time']))

    def display(self):
        for name in self.list:
            self.display_recipe(name)

    def index(self):
        print("All recipe: ")
        for name in self.list:
            print("- {}".format(name))


def add(cookbook):
    print("Please enter the recipe's name to add:\n>> ", end='')
    name = input()
    print("Please enter the list of ingredients to add: (0 for end)")
    ingredients = []
    while True:
        print(">> ", end='')
        ingredient = input()
        if ingredient == str(0):
            break
        ingredients.append(ingredient)
    print("Please enter the type of meal:\n>> ", end='')
    meal = input()
    print("Please enter the time to cook:\n>> ", end='')
    prep_time = input()
    cookbook.add(name, ingredients, meal, prep_time)


def main():
    cookbook = Book()
    cookbook.add('sandwich', ['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10)
    cookbook.add('cake', ['flour', 'sugar', 'eggs'], 'dessert', 60)
    cookbook.add('salad', ['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)

    while True:
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit\n>> ", end='')

        entry = input()
        print()
        if entry == str(1):
            add(cookbook)
        elif entry == str(2):
            print("Please enter the recipe's name to remove:\n>> ", end='')
            name = input()
            cookbook.remove(name)
        elif entry == str(3):
            print("Please enter the recipe's name to get its details:\n>> ", end='')
            name = input()
            cookbook.display_recipe(name)
        elif entry == str(4):
            cookbook.index()
        elif entry == str(5):
            print("CookBook closed.")
            return
        else:
            print("This option does not exist, please type the corresponding number.")


if __name__:
    main()
