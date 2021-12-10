from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def home_page():

    dojos = Dojo.get_all_dojos()

    return render_template ('dojos.html', dojos = dojos)

@app.post('/create/dojo')
def create_dojo():

    new_dojo = Dojo.create_dojo(request.form)

    return redirect('/dojos')

@app.post('/create/ninja')
def create_ninja():

    print (request.form)
    dojo_id = request.form['dojo_id']
    new_ninja = Ninja.create_ninja(request.form)

    return redirect(f'/dojos/{dojo_id}')

@app.route('/dojos/<int:id>')
def ninja_list(id):

    ninjas = Ninja.get_all_ninjas(id)

    return render_template('display_ninjas.html', ninjas = ninjas)

@app.route('/ninja/new')
def new_ninja_form():

    dojos = Dojo.get_all_dojos()

    return render_template ('add_ninja.html', dojos = dojos)

