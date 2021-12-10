
from flask_app import app
from flask_app.models import users



@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 