import mysql.connector

# Establishing connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NationalSassy!23",
    database="cooking_assistant"
)

# Creating a cursor object to interact with the database
mycursor = mydb.cursor()

# Table creation SQL statements
table_creation_statements = [
    """CREATE TABLE IF NOT EXISTS `ingredients` (
        `ingredient_id` int NOT NULL AUTO_INCREMENT,
        `ingredient_name` varchar(255) DEFAULT NULL,
        PRIMARY KEY (`ingredient_id`),
        UNIQUE KEY `ingredient_name` (`ingredient_name`)
    ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci""",
    
    """CREATE TABLE IF NOT EXISTS `recipe_ingredients` (
        `recipe_id` int NOT NULL,
        `ingredient_id` int NOT NULL,
        PRIMARY KEY (`recipe_id`,`ingredient_id`),
        KEY `ingredient_id` (`ingredient_id`),
        CONSTRAINT `recipe_ingredients_ibfk_1` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`),
        CONSTRAINT `recipe_ingredients_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci""",
    
    """CREATE TABLE IF NOT EXISTS `recipes` (
        `recipe_id` int NOT NULL AUTO_INCREMENT,
        `recipe_name` varchar(255) DEFAULT NULL,
        PRIMARY KEY (`recipe_id`),
        UNIQUE KEY `recipe_name` (`recipe_name`)
    ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
]

# Data insertion SQL statements
# Whenever you are adding things to the database make sure you are adding them in this order: recipes, ingredients, cookid. if you do not the program will give you an error.
#You should uncomment what you need to add in your databse and comment it back when you are done or you will get an error.
data_insertion_statements = {
    
    "ingredients": [
        #"""INSERT INTO `ingredients` VALUES (3,'garlic'),(4,'olive oil'),(1,'pasta'),(5,'sugar'),(2,'tomato')"""
        #"""INSERT INTO `ingredients` VALUES (6,'hot sauce'),(7,'cheese'),(8,'beef'),(9,'pork'),(10,'chicken'),(11,'noodles'),(12,'sausage'),(13,'marinara sauce'),(14,'eggplant'),(15,'lettuce'),(16,'croutons'),(17,'ceasar dressing'),(18,'dough')"""
    ],
    "cookid": [
        #"""INSERT INTO `cookid` VALUES (1,1),(2,1),(1,2),(1,3),(2,3),(1,4),(2,4),(3,5)"""
        #"""INSERT INTO `cookid` VALUES (4,6),(5,8),(6,7),(7,9),(4,10),(8,3),(8,7),(8,11),(8,8),(8,12),(8,13),(9,11),(9,13),(9,14),(9,3),(10,14),(10,13),(10,7),(11,15),(11,7),(11,4),(11,16),(11,17),(12,13),(12,18),(12,7),(12,4)"""
    ],
    "recipes": [
        #"""INSERT INTO `recipes` VALUES (3,'Cake'),(2,'Chicken Stir-Fry'),(1,'Pasta with Tomato Sauce')"""
       # """INSERT INTO `recipes` VALUES (4,'Hot Wings'),(5,'Hamburger'),(6,'Mac and Cheese'),(7,'Pork Chops'),(8,'Lasagna'),(9,'Spaghetti'),(10,'Eggplant Parmesan'),(11,'Ceasar Salad'),(12,'Margherita Pizza')"""
    ]
}

# Creating tables
for statement in table_creation_statements:
    mycursor.execute(statement)


# Inserting data
for table, statements in data_insertion_statements.items():
    for statement in statements:
        mycursor.execute(statement)
    
# Remove or comment out the used INSERT INTO statements
# new_ingredients_insertion_statements.clear()  # This clears the list

# OR you can comment out the used statements
# for statement in new_ingredients_insertion_statements:
#     # mycursor.execute(statement)

# Define the values you want to delete from the cookid table
recipe_id_to_delete = 9
ingredient_id_to_delete = 14

# Define the SQL statement to delete the entry
delete_statement = "DELETE FROM cookid WHERE recipe_id = %s AND ingredient_id = %s"

# Execute the delete statement with the specified recipe_id
mycursor.execute(delete_statement, (recipe_id_to_delete,ingredient_id_to_delete))
        
# Committing the changes
mydb.commit()

# Displaying the tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# Close the cursor and database connection
mycursor.close()
mydb.close()

