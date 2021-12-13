# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, redirect
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DB = 'login_and_reg'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (data['password'] != data['confirm_password']):
            flash("Passwords do not match")
            is_valid = False
        if not EMAIL_REGEX.match (data['email']):
            flash("Not a valid email")
            is_valid = False
        return is_valid

    @staticmethod
    def login_attempt():
        query = "SELECT * FROM users;"

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query,data)
        # Create an empty list to append our instances of friends
        if not results:
            flash("Invalid Email/Password")
            return False
        
        return results[0]


    @classmethod
    def create(cls, data ):
        query = '''
                INSERT INTO users ( first_name , last_name , email , passowrd, created_at, updated_at ) 
                VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW(), NOW());
                '''
        connectToMySQL(DB).query_db( query, data )

        query = "SELECT * FROM users WHERE email = %(email)s;"

        data = connectToMySQL(DB).query_db( query, data )

        print(data)
        
        return (data)



    