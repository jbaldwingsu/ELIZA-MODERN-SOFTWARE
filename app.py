# Import necessary modules
from flask import Flask, render_template, request, jsonify
import mysql.connector
from cookassist import connect_to_database, find_ingredients, find_recipes_by_ingredients, fetch_all_ingredients, fetch_all_recipes

# Initialize Flask app
app = Flask(__name__)

# Connect to MySQL database
db_connection = connect_to_database()
cursor = db_connection.cursor()

# Main route to render the index.html template
@app.route("/")
def index():
    return render_template('index.html')

# Route to handle user choice and continue conversation
@app.route('/chat', methods=['POST'])
def chat():
    # Get user choice from the form
    user_choice = request.form['choice']
    response = ""

    # Handle user choice
    if user_choice == "1":
        # Fetch all recipes
        recipes_menu = fetch_all_recipes(cursor)
        response = "\nPlease enter the number to the recipe:\n"
        for i, recipe in enumerate(recipes_menu, start=1):
            response += f"{i}. {recipe}\n"
    elif user_choice == "2":
        # Fetch all ingredients
        ingredients_list = fetch_all_ingredients(cursor)
        response = "\nHere are all the ingredients available:\n"
        for i, ingredient in enumerate(ingredients_list, start=1):
            response += f"{i}. {ingredient}\n"
    else:
        response = "Invalid choice. Please enter 1 or 2."

    return {'response': response}

# Route to handle user input for finding recipes by ingredient
@app.route('/recipes-by-ingredient', methods=['POST'])
def get_recipes_by_ingredient():
    ingredient = request.json["ingredient"]
    recipes = find_recipes_by_ingredients(cursor, ingredient)
    return jsonify({"recipes": recipes})

# Route to handle getting all ingredients
@app.route('/ingredients', methods=['GET'])
def get_all_ingredients():
    ingredients = fetch_all_ingredients(cursor)
    return jsonify({"ingredients": ingredients})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
