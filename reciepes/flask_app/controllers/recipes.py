from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.controllers.users import user_home
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt       
bcrypt = Bcrypt(app) 

@app.route("/recipe/create/form")
def create_recipe_form():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('create_recipe.html')

@app.post("/recipe/create")
def create_recipe():
    data ={
            'under_thirty' : 0,
            'user_id' : session['user_id'],
            **request.form
        }
    print(data)

    Recipe.create_recipe(data)

    return redirect('/user/home')

@app.route("/recipe/view/<int:id>")
def view_recipe(id):
    data ={
        'id': id
    }
    recipe = Recipe.get_recipe_by_id(data)

    return render_template('view_recipe.html', recipe = recipe)

@app.route("/recipe/edit/<int:id>")
def edit_recipe(id):
    data ={
        'id': id
    }
    recipe = Recipe.get_recipe_by_id(data)

    return render_template('edit_recipe.html', recipe = recipe)

@app.post("/recipe/edit/action/<int:id>")
def edit_recipe_action(id):
    data ={
        'id' : id,
        'under_thirty': 0,
        **request.form
    }
    recipe = Recipe.edit_recipe(data)
    return redirect('/user/home')

@app.route("/recipe/delete/<int:id>")
def delete_recipe_action(id):
    data ={
        'id': id
    }

    recipe = Recipe.delete_recipe_by_id(data)

    return redirect ('/user/home')
