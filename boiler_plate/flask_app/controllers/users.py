from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)