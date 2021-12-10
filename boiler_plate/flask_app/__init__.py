# pretty much always need this for every flask app
from flask import Flask
app = Flask(__name__)
app.secret_key = "myverysecretkey"

DB = "papa_jims_schema" 