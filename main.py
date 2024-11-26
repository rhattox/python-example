from flask import Flask, jsonify, request
from routes.register import register_blueprint

# Create the Flask app
app = Flask(__name__)


# Route for the home page
@app.route('/')
def home():
    return "Welcome to Flask!"


app.register_blueprint(register_blueprint)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
