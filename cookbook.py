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
    
    """CREATE TABLE IF NOT EXISTS `cookid` (
        `recipe_id` int NOT NULL,
        `ingredient_id` int NOT NULL,
        PRIMARY KEY (`recipe_id`,`ingredient_id`),
        KEY `ingredient_id` (`ingredient_id`),
       # CONSTRAINT `recipe_ingredients_ibfk_1` FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`recipe_id`),
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
        #"""INSERT INTO `ingredients` VALUES (19,'bell pepper'),(20,'broccoli'),(21,'soy sauce'),(22,'flour'),(23,'butter'),(24, 'eggs'),(25, 'milk'),(26, 'baking powder'),(27, 'vanilla extract'),(28, 'salt'),(29, 'pepper'),(30, 'garlic powder'),(31, 'paprika'),(32, 'vegetable oil'),(33, 'onion'),(34, 'onion powder'),(35, 'tomato paste'),(36, 'parsely'),(37, 'basil leaves'),(38, 'carrots'),(39, 'celery'),(40, 'potatoes'),(41, 'taco seasoning'),(42, 'tortillas'),(43, 'sour cream'),(44, 'baking soda'),(45, 'chocolate chips'),(46, 'mushrooms'),(47, 'worcestershire sauce')"""
        """INSERT INTO `ingredients` VALUES (48, 'salmon fillet'),(49, 'lemon'),(50, 'dill'),(51, 'thyme'),(52, 'tofu'),(53, 'ginger'),(54, 'honey'),(55, 'sesame oil'),(56, 'cornstarch'),(57, 'rice'),(58, 'italian seasoning'),(59, 'rosemary'),(60, 'peas'),(61, 'corn'),(62, 'black beans'),(63, 'cumin'),(64, 'chili powder'),(65, 'shrimp'),(66, 'white wine'),(67, 'sweet potatoes'),(68, 'cilantro'),(69, 'cucumber'),(70, 'cherry tomatoes'),(71, 'olives'),(72, 'red onions'),(73, 'greek dressing'),(74, 'beef strips'),(75, 'oyster sauce'),(76, 'rice vinegar'),(77, 'dijon mustard'),(78, 'spinach'),(79, 'avocado'),(80, 'salsa'),(81, 'tortilla chips'),(82, 'chickpeas'),(83, 'apricots'),(84, 'moroccan spice'),(85, 'couscous'),(86, 'zucchini'),(87, 'herbs'),(88, 'green onions'),(89, 'butternut squash'),(90, 'coconut milk'),(91, 'curry powder'),(92, 'nutmeg'),(93, 'cinnamon'),(94, 'greek yogurt'),(95, 'oregano'),(96, 'quinoa'),(97, 'red pepper flakes'),(98, 'pizza dough'),(99, 'bbq sauce'),(100, 'pineapple'),(101, 'bread'),(102, 'granola'),(103, 'strawberries'),(104, 'blueberries'),(105, 'raspberries'),(106, 'banana'),(107, 'oat flour'),(108, 'syrup'),(109, 'almond milk'),(110, 'chia seeds'),
            (111, 'coconut flakes'),(112, 'oats'),(113, 'apples'),(114, 'brown sugar'),(115, 'dark chocolate'),(116, 'heavy cream'),(117, 'marshmallows'),(118, 'rice krispie cereal')"""

    ],
    "cookid": [
        #"""INSERT INTO `cookid` VALUES (1,1),(2,1),(1,2),(1,3),(2,3),(1,4),(2,4),(3,5)"""
        #"""INSERT INTO `cookid` VALUES (4,6),(5,8),(6,7),(7,9),(4,10),(8,3),(8,7),(8,11),(8,8),(8,12),(8,13),(9,11),(9,13),(9,3),(10,14),(10,13),(10,7),(11,15),(11,7),(11,4),(11,16),(11,17),(12,13),(12,18),(12,7),(12,4)"""
        #"""INSERT INTO `cookid` VALUES (2,20),(2,21),(2,10),(3,22),(3,23),(3,24),(3,25),(3,26),(3,27),(3,28),(4,23),(4,22),(4,28),(4,29),(4,30),(4,31),(4,32),(5,28),(5,29),(5,32),(5,33),(6,1),(6,23),(6,25),(6,28),(6,29),(7,28),(7,29),(7,30),(7,31),(7,32),(7,34),(8,28),(8,29),(8,24),(8,35),(8,36),(8,33),(9,28),(9,29),(10,28),(10,24),(10,37),(12,28),(12,29),(12,37),(13,28),(13,29),(13,3),(13,2),(13,33),(13,38),(13,39),(13,40),(14,8),(14,41),(14,42),(14,15),(14,2),(14,7),(14,43),(15,22),(15,23),(15,5),(15,24),(15,27),(15,28),(15,44),(15,45),(16,8),(16,33),(16,46),(16,43),(16,47),(16,22),(16,23),(16,11),(17,22),(17,25),(17,24),(17,5),(17,26),(17,28),(17,23)"""
        """INSERT INTO `cookid` VALUES(18, 48),(18, 23),(18, 49),(18, 3),(18, 87),(18, 50),(18, 36),(18, 51),(18, 28),(18, 29),(19, 52),(19, 19),(19, 20),(19, 38),(19, 33),(19, 3),(19, 53),(19, 21),(19, 54),(19, 55),(19, 56),(20, 19),(20, 8),(20, 57),(20, 33),(20, 3),(20, 35),(20, 7),(20, 28),(20, 29),(21, 10),(21, 49),(21, 3),
                                    (21, 4),(21, 87),(21, 59),(21, 51),(21, 28),(21, 29),(22, 57),(22, 60),(22, 38),(22, 61),(22, 19),(22, 24),(22, 21),(22, 55),(22, 3),(22, 53),(22, 88),(23, 62),(23, 61),(23, 19),(23, 33),(23, 7),(23, 42),(23, 63),(23, 64),(23, 28),(23, 29),(24, 65),(24, 3),(24, 23),(24, 49),(24, 66),(24, 36),
                                    (24, 28),(24, 29),(25, 67),(25, 62),(25, 2),(25, 33),(25, 19),(25, 3),(25, 64),(25, 63),(25, 31),(25, 7),(25, 68),(26, 10),(26, 69),(26, 15),(26, 70),(26, 71),(26, 7),(26, 72),(26, 73),(27, 74),(27, 20),(27, 3),(27, 53),(27, 21),(27, 75),(27, 55),(27, 56),(27, 76),(28, 57),(28, 46),(28, 33),
                                    (28, 3),(28, 66),(28, 7),(28, 23),(28, 51),(29, 10),(29, 54),(29, 77),(29, 3),(29, 4),(29, 28),(29, 29),(29, 51),(30, 10),(30, 78),(30, 7),(30, 3),(30, 4),(30, 28),(30, 29),(31, 8),(31, 15),(31, 2),(31, 62),(31, 61),(31, 79),(31, 7),(31, 80),(31, 43),(31, 81),(32, 82),(32, 2),(32, 33),(32, 3),(32, 19),
                                    (32, 38),(32, 83),(32, 84),(32, 85),(33, 19),(33, 86),(33, 46),(33, 70),(33, 4),(33, 3),(33, 87),(33, 28),(33, 29),(34, 48),(34, 54),(34, 21),(34, 3),(34, 53),(34, 55),(34, 88),(35, 10),(35, 15),(35, 17),(35, 7),(35, 42),(36, 89),(36, 33),(36, 3),(36, 90),(36, 91),(36, 92),(36, 93),(36, 28),
                                    (36, 29),(37, 94),(37, 49),(37, 3),(37, 4),(37, 95),(37, 28),(37, 29),(38, 14),(38, 86),(38, 19),(38, 2),(38, 33),(38, 3),(38, 4),(38, 51),(38, 37),(39, 19),(39, 96),(39, 62),(39, 61),(39, 2),(39, 33),(39, 3),(39, 63),(39, 64),(39, 7),(40, 65),(40, 1),(40, 23),(40, 3),(40, 49),(40, 36),(40, 97),
                                    (40, 7),(41, 98),(41, 99),(41, 10),(41, 100),(41, 72),(41, 7),(41, 68),(42, 101),(42, 79),(42, 24),(42, 28),(42, 29),(42, 70),(43, 94),(43, 103),(43, 104),(43, 105),(43, 54),(44, 106),(44, 24),(44, 107),(44, 26),(44, 93),(44, 108),(45, 106),(45, 78),(45, 94),(45, 109),(45, 102),(45, 103),(45, 104),
                                    (45, 105),(45, 110),(45, 111),(46, 24),(46, 62),(46, 79),(46, 80),(46, 7),(46, 42),(47, 110),(47, 27),(47, 54),(47, 102),(47, 103),(47, 104),(48, 113),(48, 112),(48, 22),(48, 114),(48, 93),(48, 23),(48, 49),(49, 115),(49, 116),(49, 5),(49, 27),(50, 117),(50, 23),(50, 118),(51, 103),(51, 104),
                                    (51, 105),(51, 22),(51, 112),(51, 114),(51, 23),(51, 93),(52, 23),(52, 22),(52, 24),(52, 5),(52, 49)"""
    ],
    "recipes": [
        #"""INSERT INTO `recipes` VALUES (3,'Cake'),(2,'Chicken Stir-Fry'),(1,'Pasta with Tomato Sauce')"""
        #"""INSERT INTO `recipes` VALUES (4,'Hot Wings'),(5,'Hamburger'),(6,'Mac and Cheese'),(7,'Pork Chops'),(8,'Lasagna'),(9,'Spaghetti'),(10,'Eggplant Parmesan'),(11,'Ceasar Salad'),(12,'Margherita Pizza')"""
        #"""INSERT INTO `recipes` VALUES (13,'vegetable soup'),(14,'beef taco'),(15,'chocolate chip cookies'),(16,'beef stroganoff'),(17,'pancakes')"""
        """INSERT INTO `recipes` VALUES (18, 'Grilled Salmon with Lemon Herb Butter'),(19, 'Teriyaki Tofu Stir-Fry'),(20, 'Stuffed Bell Peppers'),(21, 'Lemon Garlic Roasted Chicken'),(22, 'Veggie Fried Rice'),(23, 'Black Bean and Corn Quesadillas'),(24, 'Lemon Garlic Shrimp Scampi'),(25, 'Baked Sweet Potatoes with Black Bean Chili'),(26, 'Mediterranean Grilled Chicken Salad'),(27, 'Beef and Broccoli Stir-Fry'),
                                        (28, 'Mushroom Risotto'),(29, 'Baked Honey Mustard Chicken'),(30, 'Spinach and Feta Stuffed Chicken Breast'),(31, 'Taco Salad'),(32, 'Moroccan Chickpea Tagine'),(33, 'Grilled Veggie Skewers'),(34, 'Honey Garlic Glazed Salmon'),(35, 'Chicken Caesar Wraps'),(36, 'Butternut Squash Soup'),(37, 'Greek Yogurt Chicken Kabobs'),
                                        (38, 'Ratatouille'),(39, 'Quinoa Stuffed Bell Peppers'),(40, 'Garlic Butter Shrimp Pasta'),(41, 'Hawaiian BBQ Chicken Pizza'),(42, 'Avocado Toast with Poached Egg'),(43, 'Greek Yogurt Parfait'),(44, 'Banana Pancakes'),(45, 'Smoothie Bowl'),(46, 'Breakfast Burrito'),(47, 'Chia Seed Pudding'),(48, 'Apple Crisp'),
                                        (49, 'Chocolate Mousse'),(50, 'Rice Krispies Treats'),(51, 'Berry Crumble'),(52, 'Lemon Bars')"""

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
#recipe_id_to_delete = 9
#ingredient_id_to_delete = 14

# Define the SQL statement to delete the entry
#delete_statement = "DELETE FROM cookid WHERE recipe_id = %s AND ingredient_id = %s"

# Execute the delete statement with the specified recipe_id
#mycursor.execute(delete_statement, (recipe_id_to_delete,ingredient_id_to_delete))
        
# Committing the changes
mydb.commit()

# Displaying the tables
mycursor.execute("SHOW TABLES")
print("Tables:")
tables = mycursor.fetchall()  # Fetch all the results from the SHOW TABLES query
for table in tables:
    table_name = table[0]
    print(f"\nContents of '{table_name}' table:")
    mycursor.execute(f"SELECT * FROM {table_name}")
    for row in mycursor.fetchall():
        print(row)

# Close the cursor and database connection
mycursor.close()
mydb.close()

