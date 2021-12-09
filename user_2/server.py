
from flask import Flask, redirect, render_template, redirect, request

app= Flask(__name__)

from user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route('/user/new')
def createuser():
    return render_template("newuser.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.create(request.form)
    return redirect('/users')


@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 