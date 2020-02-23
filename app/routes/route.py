from flask import Blueprint , render_template , request
from app.models.name import Name

route = Blueprint('route', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return route

@route.route('/')
def index():
    return render_template('main.html')

@route.route('/addName', methods=['POST'])
def addName():
    name = request.form['name']
    newName = Name(name=name)
    newName.insert()
    return ('Success',200)