from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# from sqlite3
from forms import RegistrationForm, LoginForm
import os


app = Flask(__name__)

posts = [
    {
        'author': 'sintayehu sermesssa',
        'title' : 'Blog post 1',
        'content' : 'first post content',
        'date_posted': 'April 28 2021',
    },
    {
        'author': 'sintayehu sermesssa',
        'title' : 'Blog post 2',
        'content' : 'first post content',
        'date_posted': 'April 29 2021',
    }
]

app.config['SECRET_KEY'] = '051277379b285b544ff835e235bf0e658e22d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/site.db '



@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', title = "Home" , posts= posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created fro {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dqqqqqede@gmail.com' and form.password.data == '2222':
            flash('You have been logged in!','success' )
            return redirect(url_for('index'))
        else:
            flash(' login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
