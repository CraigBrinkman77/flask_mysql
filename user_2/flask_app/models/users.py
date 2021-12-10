
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers.user import User
from flask_app import app


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("index.html", users = users)

@app.route('/user/new')
def createuser():
    return render_template("newuser.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/user/view/<int:id>')
def view_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template("view_user.html", user = user)

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user = user)

@app.post('/user/update/<int:id>')
def update_user(id):
    data = {
        **request.form, 'id' : id
    }
    User.update(data)
    
    return redirect(f'/user/view/{id}')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id' : id
    }
    User.delete(data)
    return redirect('/users')