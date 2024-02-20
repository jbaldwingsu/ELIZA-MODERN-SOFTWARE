import mysql.connector
import random

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="thunderbear",
        database="cooking_assistant"
    )

# Function to find recipes based on ingredients using query
def find_recipes(cursor, ingredients):
    query = """
        SELECT DISTINCT recipe_name
        FROM recipes
        INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
        INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
        WHERE ingredients.ingredient_name IN (%s)
    """
    cursor.execute(query, ingredients)
    return [row[0] for row in cursor]

# Eliza-like bot responses
def eliza_response(input_text):
    responses = [
        "Tell me more about your ingredients.",
        "Why are you interested in those ingredients?",
        "How do you feel about cooking today?"
    ]
    return random.choice(responses)

# Main function to handle user input
def main():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()
    
    print("Hi I'm Eliza, the cooking assistant!")
    print("Please enter the ingredients you have, separated by commas (e.g., pasta, tomato, garlic):")
    
    while True:     # exit statement variations for eliza
        user_input = input("> ").lower().strip()
        if user_input == "exit":
            print("Goodbye!")
        elif (user_input == "bye"):
            print("See Ya! Hope the food turns out GREAT!")
            break
        elif user_input:
            ingredients = tuple(user_input.split(", "))
            matching_recipes = find_recipes(cursor, ingredients)
            if matching_recipes:
                print("Based on your ingredients, here are some recipes we can make for you:")
                for recipe in matching_recipes:
                    print("-", recipe)
            else:
                print("Sorry, I couldn't find any recipes matching those ingredients.")
        else:
            print(eliza_response(user_input))

    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
