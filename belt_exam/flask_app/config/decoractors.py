from functools import wraps
from flask import flash, redirect, request, session
from flask_app.models.user import User

def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if 'user_id' not in session:
            flash('Please login first')
            return redirect('/')
        return func(*args,**kwargs)
    return inner
