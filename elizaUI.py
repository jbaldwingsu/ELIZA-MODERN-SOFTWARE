import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
import mysql.connector

class CookingAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()
        self.main_menu()  # Display the main menu when the CookingAssistant object is created

    def initUI(self):
        self.setWindowTitle('Cooking Assistant')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.handle_submit)
        layout.addWidget(self.submit_button)

    def initDB(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Osiris34",
            database="cooking_assistant"
        )
        self.cursor = self.db_connection.cursor()

    def main_menu(self):
        # Display the main menu options
        self.output_text.append("Hi I'm Eliza, the cooking assistant!")
        self.output_text.append("Would you like to:")
        self.output_text.append("1. Choose a recipe by number")
        self.output_text.append("2. Input an ingredient to find recipes")

    def handle_submit(self):
        user_input = self.input_text.text().strip()
        self.input_text.clear()
        self.output_text.append(f"> {user_input}")

        if user_input.lower() == "exit" or user_input.lower() == "bye":
            self.output_text.append("See you! Hope the food turns out GREAT!")
            return

        if user_input == "1":
            self.handle_choose_recipe()
        elif user_input == "2":
            self.handle_input_ingredient()
        else:
            self.output_text.append("Invalid input. Please try again.")

    def handle_choose_recipe(self):
        self.output_text.append("\nPlease enter the number of the recipe:")
        recipes_menu = self.fetch_all_recipes()
        for i, recipe in enumerate(recipes_menu, start=1):
            self.output_text.append(f"{i}. {recipe}")

    def handle_input_ingredient(self):
        self.output_text.append("\nHere are all the ingredients available:")
        ingredients_list = self.fetch_all_ingredients()
        for i, ingredient in enumerate(ingredients_list, start=1):
            self.output_text.append(f"{i}. {ingredient}")

        self.output_text.append("Please enter the number of the ingredient you'd like to find recipes for:")

        # Wait for user input and handle it
        self.submit_button.clicked.disconnect()  # Disconnect the previous signal-slot connection
        self.submit_button.clicked.connect(self.handle_ingredient_selection)

    def handle_ingredient_selection(self):
        user_input = self.input_text.text().strip()
        self.input_text.clear()
        self.output_text.append(f"> {user_input}")

        try:
            ingredient_index = int(user_input)
            ingredients_list = self.fetch_all_ingredients()  # Fetch ingredients again
            if 1 <= ingredient_index <= len(ingredients_list):
                selected_ingredient = ingredients_list[ingredient_index - 1]
                self.output_text.append(f"\nFinding recipes for {selected_ingredient}...")
                recipes = self.find_recipes_by_ingredient(selected_ingredient)
                if recipes:
                    self.output_text.append(f"Recipes that can be made with {selected_ingredient}:\n")
                    for recipe in recipes:
                        self.output_text.append("* " + recipe)
                else:
                    self.output_text.append(f"Sorry, I couldn't find any recipes with {selected_ingredient}.")
            else:
                self.output_text.append("Invalid input. Please enter a valid number corresponding to an ingredient.")
        except ValueError:
            self.output_text.append("Invalid input. Please enter a number.")

    def fetch_all_recipes(self):
        self.cursor.execute("SELECT recipe_name FROM recipes ORDER BY recipe_id")
        return [row[0] for row in self.cursor]

    def fetch_all_ingredients(self):
        self.cursor.execute("SELECT ingredient_name FROM ingredients ORDER BY ingredient_id")
        return [row[0] for row in self.cursor]

    def find_recipes_by_ingredient(self, ingredient):
        self.cursor.execute("SELECT DISTINCT recipes.recipe_name FROM recipes INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id WHERE ingredients.ingredient_name = %s ORDER BY recipes.recipe_name", (ingredient,))
        return [row[0] for row in self.cursor]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cooking_assistant = CookingAssistant()
    cooking_assistant.show()
    sys.exit(app.exec_())
