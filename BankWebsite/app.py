from flask import Flask, render_template, request, redirect, url_for, session
import secrets
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
client = MongoClient("mongodb+srv://shon:SeanSak123@cluster0.wrckk3j.mongodb.net")
db = client["Bank"]
collection = db["users"]

@app.route("/")
def loginPage():
    return render_template("login.html")

@app.route("/home")
def home():
    if 'username' in session:
        return render_template("home.html", username=session['username'], bank=session.get('bank', 'Bank information not found'))
    return redirect(url_for('loginPage'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = collection
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            users.insert_one({
                'username': request.form['username'],
                'password': request.form['password']
            })
            return redirect(url_for('home'))

        return 'Username already exists!'

    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    users = collection
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            bank = collection.find_one({'username': request.form['username']})['bank']
            session['bank'] = bank
            return redirect(url_for("home"))
        else:
            return 'Invalid password'
    else:
        return 'Invalid username'

if __name__ == "__main__":
    app.run()