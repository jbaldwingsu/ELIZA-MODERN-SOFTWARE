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

# Function to find ingredients bases on recipes using query
def find_ingredients(cursor, recipe_name):
    query = """
        SELECT ingredients.ingredient_name
        FROM recipes
        INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
        INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
        WHERE recipes.recipe_name = %s
        ORDER BY cookid.recipe_id
    """
    cursor.execute(query, (recipe_name,))
    return [row[0] for row in cursor.fetchall()]

# Function to find recipe based on ingredietns using query
def find_recipes_by_ingredients(cursor, ingredient):
    query = """
        SELECT DISTINCT recipes.recipe_name
        FROM recipes
        INNER JOIN cookid ON recipes.recipe_id = cookid.recipe_id
        INNER JOIN ingredients ON cookid.ingredient_id = ingredients.ingredient_id
        WHERE ingredients.ingredient_name = %s
        ORDER BY recipes.recipe_name
    """
    cursor.execute(query, (ingredient,))
    return [row[0] for row in cursor.fetchall()]

# Function to fetch all ingredients (Option 2)
def fetch_all_ingredients(cursor):
    query = "SELECT ingredient_name FROM ingredients ORDER BY ingredient_id"
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]

# Function to fetch all recipes from database (Option 1)
def fetch_all_recipes(cursor):
    query = "SELECT recipe_name FROM recipes ORDER BY recipe_id"
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]

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
    print("Would you like to:")
    print("1. Choose a recipe by number")
    print("2. Input an ingredient to find recipes")

    # Choice statements    
    choice = input ("> ").strip()

    if choice == "1":
        while True:
            print("\nPlease enter the number to the recipe:")
            recipes_menu = fetch_all_recipes(cursor)
            for i, recipe in enumerate (recipes_menu, start=1):
                print(f"{i}. {recipe}")
            
            user_input = input("> ").strip()
            if (user_input.lower() == "exit" or user_input.lower() == "bye"):
                print("See you! Hope the food turns out GREAT!")
                break
            elif user_input.isdigit():
                index = int(user_input)
                if 1 <= index <= len(recipes_menu):
                    selected_recipe = recipes_menu[index - 1]
                    print(f"\nFetching ingredients for {selected_recipe}...")
                    ingredients = find_ingredients(cursor, selected_recipe)
                    if ingredients:
                        print(f"Ingredients for {selected_recipe}:\n")
                        for ingredient in ingredients:
                            print("*", ingredient)
                    else:
                        print("Invalid input. Please enter a number corresponding to a recipe.")
                else:
                    print("Invalid input. Please enter a number corresponding to a recipe.")
                    break
                
                # prompts to choose menu item again (option 1)
                # continue_option - option to continue searching for ingredient/recipe (depending on original option 1 or 2)
                # switch_option - option to switch to finding opposite original option
                print("\nWould you like to get ingredients for another recipe? (yes/no)")
                continue_option = input("> ").strip().lower()
                
                if continue_option == 'no':
                    # prompts choice to choose recipes if user doesnt redo option 1
                    print("Would you like to input an ingredient to find recipes instead? (yes/no)")
                    switch_option = input(">").strip().lower()
                    if switch_option == 'yes':
                        #HARD CODE HERE
                                    print ("Here are all the ingredients available:")
                                    ingredients_list = fetch_all_ingredients(cursor)
                                    for i, ingredient in enumerate(ingredients_list, start=1):
                                                print(f"{i}. {ingredient}")

                                    while True:
                                        print("Please enter the number of the ingredient you'd like to find recipes for:")
                                        ingredient_index = input("> ").strip()
                                        if ingredient_index.isdigit():
                                            index = int(ingredient_index)
                                            if 1 <= index <= len(ingredients_list):
                                                selected_ingredient = ingredients_list[index - 1]
                                                print(f"\nFinding recipes for {selected_ingredient}...")
                                                recipes = find_recipes_by_ingredients(cursor, selected_ingredient)
                                                if recipes:
                                                        print(f"Recipes that can be made with {selected_ingredient}:\n")
                                                        for recipe in recipes:
                                                            print("*", recipe)
                                                else:
                                                    print(f"Sorry, I couldn't find any recipes with {selected_ingredient}.")
                                            else:
                                                print("Invalid input. Please enter a valid number corresponding to an ingredient.")
                                                continue #restart the loop to allow the user to input another integer
                                        else:
                                            print("Invalid input. Please enter a valid number.")
                                            continue

                                        print("\nWould you like to find recipes for another ingredient? (yes/no)")
                                        continue_option = input("> ").strip().lower()
                                        if continue_option == 'no':
                                                print("See you! Hope the food turns out GREAT")
                                                return
                                        elif continue_option != 'yes':
                                                print("Invalid input. Please enter 'yes' or 'no'.")
                                                break                      
                    elif switch_option == 'no':
                        print("See you! Hope the food turns out GREAT!")
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        
                elif continue_option != 'yes':
                    break
                    print("Invalid input. Please enter 'yes' or 'no'.")
                
                    
                  
    elif choice == "2":
        # Code for choice 2
        while True:
            print("\nHere are all the ingredients available:")
            ingredients_list = fetch_all_ingredients(cursor)
            for i, ingredient in enumerate(ingredients_list, start=1):
                print(f"{i}. {ingredient}")

            print("Please enter the number of the ingredient you'd like to find recipes for:")
            ingredient_index = input("> ").strip()
            if ingredient_index.isdigit():
                index = int(ingredient_index)
                if 1 <= index <= len(ingredients_list):
                    selected_ingredient = ingredients_list[index - 1]
                    print(f"\nFinding recipes for {selected_ingredient}...")
                    recipes = find_recipes_by_ingredients(cursor, selected_ingredient)
                    if recipes:
                        print(f"Recipes that can be made with {selected_ingredient}:\n")
                        for recipe in recipes:
                            print("-", recipe)
                    else:
                        print(f"Sorry, I couldn't find any recipes with {selected_ingredient}.")
                else:
                    print("Invalid input. Please enter a valid number corresponding to an ingredient.")
            else:
                print("Invalid input. Please enter a number.")

            # Prompt to continue finding recipes for another ingredientn
            print("\nWould you like to find recipes for another ingredient? (yes/no)")
            continue_option = input("> ").strip().lower()
            if continue_option != 'yes':
                print("Would you like to choose a recipe by number for some ingredient ideas instead? (yes/no)")
                switch_option = input(">").strip().lower()
                if switch_option == 'yes':
                    # insert logic for option 1
                        while True:
                            print("Please enter the number to the recipe option:")
                            recipes_menu = fetch_all_recipes(cursor)
                            for i, recipe in enumerate(recipes_menu, start=1):
                                print(f"{i}. {recipe}")

                            user_input = input ("> ").strip()
                            if user_input.lower() == "exit" or user_input.lower() == "bye":
                                print("See you! Hope the food turns out GREAT")
                                break
                            elif user_input.isdigit():
                                index = int(user_input)
                                if 1 <= index <= len(recipes_menu):
                                    selected_recipe = recipes_menu[index - 1]
                                    print(f"Fetching ingredients for {selected_recipe}...")
                                    ingredients = find_ingredients(cursor, selected_recipe)
                                    if ingredients:
                                        print(f"Ingredients for {selected_recipe}:\n")
                                        for ingredient in ingredients:
                                            print("*", ingredient)

                                    else:
                                        print("Invalid input. Please enter a number corresponding to a recipe.")
                                        continue

                                    print("\nWould you like to get ingredients for another recipe? (yes/no)")
                                    continue_option = input("> ").strip().lower()
                                    if continue_option == 'no':
                                        print("See you! Hope the food turns out GREAT ")
                                        return
                                    elif continue_option != 'yes':
                                         print("Invalid input. Please enter 'yes' or 'no'.")
                                         break
                                    
                elif switch_option == 'no':
                        print("See you! Hope the food turns out GREAT!")
                        break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                        
            elif continue_option != 'yes':
                break
                print("Invalid input. Please enter 'yes' or 'no'.")
                                    
               
    
    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()