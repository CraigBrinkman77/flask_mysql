from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, redirect, request
from flask_app.models.user import User
DB = 'recipes_schema'
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['recipe_name']
        self.description = data['recipe_description']
        self.instructions = data['recipe_instructions']
        self.under_thirty = data['under_thirty']
        self.user_id = data['users_id']

    @classmethod
    def create_recipe(cls, data):
        
        query = '''
                INSERT INTO recipes ( recipe_name , recipe_description, recipe_instructions , under_thirty, users_id) 
                VALUES ( %(name)s , %(description)s , %(instructions)s , %(under_thirty)s, %(user_id)s);
                '''
        connectToMySQL(DB).query_db( query, data = data )

    @classmethod
    def get_all_recipes(cls):
        query = 'Select * FROM recipes JOIN users WHERE users.id = recipes.users_id;'
        
        results = connectToMySQL(DB).query_db(query)
        
        recipes = []
        for row in results:
            recipes.append(cls(row))
        recipes.user = []
        for row in results:
            user_data = {
                **row,
                'id' : row["users.id"],
                'created_at' : row['users.created_at'],
                'update_at' : row['users.updated_at']
            }
        recipes.user.append(User(user_data))

        return recipes

    @classmethod
    def get_recipe_by_id(cls, id):
        print(id)
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL(DB).query_db(query, id)

        return cls(results[0])
    
    @classmethod
    def edit_recipe(cls, data):
        
        query = 'UPDATE recipes SET recipe_name = %(name)s,recipe_description = %(description)s,recipe_instructions = %(instructions)s,under_thirty = %(under_thirty)s WHERE id = %(id)s;'

        results = connectToMySQL(DB).query_db(query, data)

    @classmethod
    def delete_recipe_by_id(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s'
        results = connectToMySQL(DB).query_db(query, data)