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
data_insertion_statements = {
    "ingredients": [
        #"""INSERT INTO `ingredients` VALUES (3,'garlic'),(4,'olive oil'),(1,'pasta'),(5,'sugar'),(2,'tomato')"""
    ],
    "cookid": [
        #"""INSERT INTO `cookid` VALUES (1,1),(2,1),(1,2),(1,3),(2,3),(1,4),(2,4),(3,5)"""
    ],
    "recipes": [
        #"""INSERT INTO `recipes` VALUES (3,'Cake'),(2,'Chicken Stir-Fry'),(1,'Pasta with Tomato Sauce')"""
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

        
# Committing the changes
mydb.commit()

# Displaying the tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# Close the cursor and database connection
mycursor.close()
mydb.close()
