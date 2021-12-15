
from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
from flask_app.config.decoractors import login_required
bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.post('/validate')
def validate():
    #validate, if flase, circle redirect
    if not User.validate_user(request.form):
        return redirect('/registration')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    user_data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email' : request.form['email'],
    'password' : pw_hash,
    }

    user_id = User.create(user_data)
    print (user_id)

    session['user_id'] = user_id
    
    return redirect('user/home')

@app.post('/login/attempt')
def login_attempt():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)
    print (user)
    if not user:
        flash('email/password invalid')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash('email/password invalid')
        return redirect('/')
    
    session['user_id'] = user.id

    return redirect("/user/home")

@app.route('/user/home')
@login_required
def user_home():
    user = User.get_by_id({'id' : session['user_id']})
    results = Recipe.get_all_recipes()
    return render_template("home.html", recipes = results, user = user)
    
@app.route('/user/logout')
def logout():
    session.clear()
    return redirect ('/login')
    