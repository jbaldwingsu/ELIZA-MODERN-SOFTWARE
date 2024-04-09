import logging
from flask import Flask, render_template, request,session, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin #ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors
from models import db, User
# from moderneliza import Eliza  # Import your Eliza chatbot logic

from models import db, User
from moderneliza import Eliza

app = Flask(__name__)
  # Initialize your Eliza chatbot

app.config['SECRET_KEY'] = 'osiris'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)
db.init_app(app)
eliza = Eliza()
eliza.load('doctor.txt')

with app .app_context():
    db.create_all()
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

@app.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "Email already exists"}), 409

    hashed_password =bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id
    return jsonify({
        "id": new_user.id,
        "email":new_user.email
    })

@app.route('/login', methods=['POST'])
@cross_origin()
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()
    
    if user is None:
        return jsonify({"error": "Unathorixed Access"}), 401
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unathorized"}), 401
    
    session["user_id"] = user.id

    return jsonify({
        "id":user.id,
        "email": user.email
    })
    # data = request.get_json()
    # message = data['message']
    # response = eliza.respond(message)
    # return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)