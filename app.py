# code for server
import logging
from flask import Flask, render_template, request,session, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin #ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors


from cookassist import connect_to_database, find_ingredients, find_recipes_by_ingredients, fetch_all_ingredients, fetch_all_recipes

app = Flask(__name__)
  # Initialize your Eliza chatbot

app.config['SECRET_KEY'] = 'osiris'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)


# Connect to MySQL database
db_connection = connect_to_database()
cursor = db_connection.cursor()


@app.route("/")
def index():
     return render_template('index.html')

logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
@cross_origin(supports_credentials=True)
def chat():
    user_message = request.form['user_input']
    bot_response = eliza.respond(user_message)
    return {'response': bot_response}

@app.route('/recipes-by-ingredient', methods=['POST'])
@cross_origin()
def get_recipes_by_ingredient():
    ingredient = request.json["ingredient"]
    recipes = find_recipes_by_ingredients(cursor, ingredient)
    return jsonify({"recipes": recipes})

@app.route('/ingredients', methods=['GET'])
@cross_origin()
def get_all_ingredients():
    ingredients = fetch_all_ingredients(cursor)
    return jsonify({"ingredients": ingredients})


if __name__ == '__main__':
    app.run(debug=True)
    