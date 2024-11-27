from flask import Blueprint, request, jsonify
from database.register_user import register_user
from models.user import User

# Create a Blueprint for register
register_blueprint = Blueprint('register', __name__)


@register_blueprint.route('/register', methods=['POST'])
def register():
    # Ensure the request is JSON
    if not request.is_json:
        return jsonify({"error": "Invalid request, expected JSON"}), 400
    data = request.json

    user = User(name=data['name'], email=data['email'], password=data['password'])

    register_user(user)

    return jsonify(data), 200
