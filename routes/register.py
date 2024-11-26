from flask import Blueprint

# Create a Blueprint for register
register_blueprint = Blueprint('register', __name__)


@register_blueprint.route('/register')
def register():
    return "Welcome to Register Page!"
