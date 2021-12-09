from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.config.mysqlconnection import connectToMySQL

class Create:

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_schema').query_db( query, data )