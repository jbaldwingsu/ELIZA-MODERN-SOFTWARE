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
# def find_recipes(cursor, ingredients):
#     query = """
#         SELECT DISTINCT recipe_name
#         FROM recipes
#         INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
#         INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
#         WHERE ingredients.ingredient_name IN (%s)
#     """
#     cursor.execute(query, ingredients)
#     return [row[0] for row in cursor]

# Function to find ingredients bases on recipes using query
def find_ingredients (cursor, recipe_name):
    query = """
        SELECT ingredient_name
        FROM recipes
        INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
        INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
        WHERE recipes.recipe_name = %s
    """

    cursor.execute(query, (recipe_name,))
    return [row[0] for row in cursor]

# Function to fetch all recipes from database
def fetch_all_recipes(cursor):
    cursor.execute("SELECT recipe_name FROM recipes")
    return [row[0] for row in cursor]

# Eliza-like bot responses (CURRENTLY NOT NEEDED)
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
    #print("Please enter the ingredients you have, separated by commas (e.g., pasta, tomato, garlic):")
    print("Please enter an item from our menu to view the recipe's ingredients.")
    
    recipes_menu = fetch_all_recipes(cursor)
    for i, recipe in enumerate(recipes_menu, start = 1):
        print (f"{i}. {recipe}")
    
    while True:     # exit statement variations for eliza
        user_input = input("> ").strip()
        if user_input.lower() == "exit":
            print("See Ya! Hope the food turns out GREAT!")
            break
        elif (user_input.lower() == "bye"):
            print("See Ya! Hope the food turns out GREAT!")
            break

        elif user_input.isdigit():
            index = int(user_input)
            if 1 <= index <= len(recipes_menu):
                selected_recipe = recipes_menu[index - 1]
                print(f"Fetching ingredients for {selected_recipe}...")
                ingredients = find_ingredients(cursor, selected_recipe)
                if ingredients:
                    print(f"Ingredients forn {selected_recipe}:")
                    for ingredient in ingredients:
                        print("-", ingredient)
                else:
                    print (f"Sorry, I couldn't find any recipes matching {selected_recipe}.")
            else: 
                print ("Invalid input. Please enter a number corresponding to a recipe.")
        else:
            print (eliza_response(user_input))

        # elif user_input:
        #     ingredients = tuple(user_input.split(", "))
        #     matching_recipes = find_recipes(cursor, ingredients)
        #     if matching_recipes:
        #         print("Based on your ingredients, here are some recipes we can make for you:")
        #         for recipe in matching_recipes:
        #             print("-", recipe)
        #     else:
        #         print("Sorry, I couldn't find any recipes matching those ingredients.")
        # else:
        #     print(eliza_response(user_input))

    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
