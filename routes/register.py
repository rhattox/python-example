from flask import Blueprint, request, jsonify
from database.register_user import register_user

# Create a Blueprint for register
register_blueprint = Blueprint('register', __name__)


@register_blueprint.route('/register', methods=['POST'])
def register():
    # Ensure the request is JSON
    if not request.is_json:
        return jsonify({"error": "Invalid request, expected JSON"}), 400
    data = request.json
    print(data['name'])
    print(data['email'])
    print(data['password'])

    register_user(data['name'], data['email'], data['password'])

    return jsonify(data), 200
