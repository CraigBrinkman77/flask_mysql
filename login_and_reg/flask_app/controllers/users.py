from werkzeug import datastructures
from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt       
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

    #if validate comes back true, create user and store in session
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
    session['logged_in'] = True
    return redirect('user/home')

@app.route('/user/home')
def user_home():
    if (session['logged_in'] == False):
        return redirect('/login')
    print (session['user_id'])
    return render_template("home.html")
    
@app.route('/user/logout')
def logout():
    session.clear()
    return redirect ('/login')
    


    
@app.post('/login/attempt')
def login_attempt():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print (user_in_db)
    if not user_in_db:
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db['passowrd'], request.form["password"]):
    
        flash("Invalid Email/Password")
        return redirect('/')
    
    session['user_id'] = user_in_db
    
    return redirect("/user/home")