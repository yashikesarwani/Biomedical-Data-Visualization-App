from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient.query import Q


db = GraphDatabase("http://localhost:7474", username="neo4j", password="saurabhk")


app = Flask(__name__)

app.config['SECRET_KEY'] = '0a54d3c876facf83ef5b4106e8e002d7'


@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)    

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'yashikesarwani092@gmail.com' and form.password.data == 'yashikes':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
          

if __name__ == "__main__":
    app.run(debug = True)
