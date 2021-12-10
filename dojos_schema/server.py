from flask import Flask, render_template, request, redirect
from flask_app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 