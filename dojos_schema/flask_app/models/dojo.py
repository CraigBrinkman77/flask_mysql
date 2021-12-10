# the function that will return an instance of a connection
from werkzeug.wrappers import request
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.ninja import Ninja
DB = 'dojoschema'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    

    @classmethod
    def get_one_dojo(cls, data):
        
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;'
        
        results = connectToMySQL(DB).query_db(query, data = data)

        dojo = cls(results[0])
        
        dojo.ninjas = []

        for row in results:
            ninja_data={
                **row,
                'id' : row['ninjas.id'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(ninja_data))

        return dojo

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at)  VALUES (%(new_dojo)s, now(), now());"


        results = connectToMySQL(DB).query_db(query, data = data)