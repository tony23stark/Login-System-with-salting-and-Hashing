from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
import os
from dotenv import load_dotenv





load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        
        salt = bcrypt.gensalt()
       
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.salt = salt.decode('utf-8')
        self.password_hash = password_hash.decode('utf-8')

    def check_password(self, password):
        
        password_hash = bcrypt.hashpw(password.encode('utf-8'), self.salt.encode('utf-8'))
        return password_hash.decode('utf-8') == self.password_hash


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        


        session['debug_hash'] = user.password_hash
        session['debug_salt'] = user.salt

        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Login successful!')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please login first')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template('profile.html', username=user.username)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out')
    return redirect(url_for('home'))



@app.route('/debug')
def debug():
    if 'debug_hash' in session and 'debug_salt' in session:
        return render_template('debug.html', 
                             password_hash=session['debug_hash'],
                             salt=session['debug_salt'])
    return "No debug information available. Please register a new account first."

if __name__ == '__main__':
    app.run(debug=True) 