from flask_app import app

from flask_app.controllers import users
from flask_app.controllers import recipes


@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 