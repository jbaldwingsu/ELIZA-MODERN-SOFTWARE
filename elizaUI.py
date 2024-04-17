import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QTextEdit, QVBoxLayout, QWidget, QInputDialog
from PyQt5.QtGui import QColor, QTextCursor


import mysql.connector


class CookingAssistantApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cooking Assistant")
        self.setGeometry(100, 100, 1000, 800)
        self.setStyleSheet("background-color: #333; color: white;")

        layout = QVBoxLayout()

        title_label = QLabel("🍳 Cooking Assistant 🍲")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        layout.addWidget(title_label)

        self.info_label = QLabel("Hi, I'm Eliza, your cooking assistant! How can I help you today?")
        self.info_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.info_label)

        self.option_combobox = QComboBox()
        self.option_combobox.addItem("Choose a recipe by number")
        self.option_combobox.addItem("Input an ingredient to find recipes")
        self.option_combobox.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.option_combobox)

        self.output_textedit = QTextEdit()
        self.output_textedit.setStyleSheet("font-size: 14px; background-color: #444; color: white;")
        layout.addWidget(self.output_textedit)

        self.go_button = QPushButton("Submit")
        self.go_button.clicked.connect(self.handle_go_button)
        self.go_button.setStyleSheet("font-size: 16px; background-color: #555; color: white;")
        layout.addWidget(self.go_button)

        self.dark_mode_button = QPushButton("Dark Mode")
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)
        self.dark_mode_button.setStyleSheet("font-size: 16px; background-color: #555; color: white;")
        layout.addWidget(self.dark_mode_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.db_connection = self.connect_to_database()
        self.cursor = self.db_connection.cursor()

    def connect_to_database(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Osiris34",
            database="cooking_assistant"
        )

    def find_ingredients(self, recipe_name):
        query = """
            SELECT ingredient_name
            FROM recipes
            INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
            INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
            WHERE recipes.recipe_name = %s
            ORDER BY cookid.recipe_id
        """
        self.cursor.execute(query, (recipe_name,))
        return [row[0] for row in self.cursor]

    def fetch_all_recipes(self):
        self.cursor.execute("SELECT recipe_name FROM recipes ORDER BY recipe_id")
        return [row[0] for row in self.cursor]

    def find_recipes_by_ingredients(self, ingredient_name):
        query = """
            SELECT DISTINCT recipes.recipe_name
            FROM recipes
            INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
            INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
            WHERE ingredients.ingredient_name = %s
            ORDER BY recipes.recipe_name
        """
        self.cursor.execute(query, (ingredient_name,))
        return [row[0] for row in self.cursor]

    def handle_go_button(self):
        self.output_textedit.clear()
        choice = self.option_combobox.currentText()

        if choice == "Choose a recipe by number":
            self.output_textedit.append("Please enter the number of the recipe:")
            recipes_menu = self.fetch_all_recipes()
            for i, recipe in enumerate(recipes_menu, start=1):
                self.output_textedit.append(f"{i}. {recipe}")

            selected_index, ok_pressed = QInputDialog.getInt(
                self, "Recipe Selection", "Enter the number of the recipe:", 1, 1, len(recipes_menu)
            )
            if ok_pressed:
                selected_recipe = recipes_menu[selected_index - 1]
                self.output_textedit.append(f"\nFetching ingredients for {selected_recipe}...")
                ingredients = self.find_ingredients(selected_recipe)
                if ingredients:
                    self.output_textedit.append(f"\nIngredients for {selected_recipe}:\n")
                    for ingredient in ingredients:
                        self.output_textedit.append(f"* {ingredient}")
                else:
                    self.output_textedit.append("Invalid input. Please enter a number corresponding to a recipe.")

        elif choice == "Input an ingredient to find recipes":
            selected_ingredient, ok_pressed = QInputDialog.getText(
                self, "Ingredient Selection", "Enter the name of the ingredient:"
            )
            if ok_pressed:
                self.output_textedit.append(f"\nFinding recipes for {selected_ingredient}...")
                recipes = self.find_recipes_by_ingredients(selected_ingredient)
                if recipes:
                    self.output_textedit.append(f"Recipes that can be made with {selected_ingredient}:\n")
                    for recipe in recipes:
                        self.output_textedit.append(f"- {recipe}")
                else:
                    self.output_textedit.append(f"Sorry, I couldn't find any recipes with {selected_ingredient}.")

    def fetch_all_ingredients(self):
        self.cursor.execute("SELECT ingredient_name FROM ingredients ORDER BY ingredient_id")
        return [row[0] for row in self.cursor]

    def toggle_dark_mode(self):
        if self.dark_mode_button.text() == "Dark Mode":
            self.setStyleSheet("background-color: #222; color: white;")
            self.option_combobox.setStyleSheet("font-size: 16px; color: white;")
            self.output_textedit.setStyleSheet("font-size: 14px; background-color: #333; color: white;")
            self.go_button.setStyleSheet("font-size: 16px; background-color: #444; color: white;")
            self.dark_mode_button.setStyleSheet("font-size: 16px; background-color: #444; color: white;")
            self.dark_mode_button.setText("Light Mode")
        else:
            self.setStyleSheet("background-color: #fff; color: black;")
            self.option_combobox.setStyleSheet("font-size: 16px; color: black;")
            self.output_textedit.setStyleSheet("font-size: 14px; background-color: #eee; color: black;")
            self.go_button.setStyleSheet("font-size: 16px; background-color: #ccc; color: black;")
            self.dark_mode_button.setStyleSheet("font-size: 16px; background-color: #ccc; color: black;")
            self.dark_mode_button.setText("Dark Mode")

    def closeEvent(self, event):
        self.cursor.close()
        self.db_connection.close()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = app.palette()
    palette.setColor(palette.Window, QColor(53, 53, 53))
    palette.setColor(palette.WindowText, QColor(255, 255, 255))
    palette.setColor(palette.Base, QColor(25, 25, 25))
    palette.setColor(palette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(palette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(palette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(palette.Text, QColor(255, 255, 255))
    palette.setColor(palette.Button, QColor(53, 53, 53))
    palette.setColor(palette.ButtonText, QColor(255, 255, 255))
    palette.setColor(palette.BrightText, QColor(255, 0, 0))
    palette.setColor(palette.Link, QColor(42, 130, 218))
    palette.setColor(palette.Highlight, QColor(42, 130, 218))
    palette.setColor(palette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

    window = CookingAssistantApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
