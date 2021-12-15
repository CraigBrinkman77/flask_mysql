# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, redirect, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DB = 'recipes_schema'

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
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(data['password']) < 7:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if (data['password'] != data['confirm_password']):
            flash("Passwords do not match")
            is_valid = False
        if not EMAIL_REGEX.match (data['email']):
            flash("Not a valid email")
            is_valid = False
        if User.get_by_email({ 'email' : data['email']}):
            flash("Email is already in use")
            is_valid = False
        return is_valid

    # @staticmethod
    # def login_attempt():
    #     if not (User.get_by_email(data = { 'email' : request.form['email']})):
    #         flash("Email is not associated with account")
    #         return redirect('/login')
        
    #     User.get_by_email(data = { 'email' : request.form['email']})


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query,data)
        print (results)
        # Create an empty list to append our instances of friends
        if not results:
            return False
        
        return cls(results[0])


    @classmethod
    def create(cls, data):
        query = '''
                INSERT INTO users ( first_name , last_name , email , password) 
                VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s);
                '''
        user_id = connectToMySQL(DB).query_db( query, data)

        return user_id

    @classmethod
    def get_by_id(cls,data):

        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL(DB).query_db( query, data)
        
        user = cls(results[0])

        return user
    