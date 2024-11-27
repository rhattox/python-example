#
# This is the main file.
# When running python application, this will be the entrypoint
# python3 main.py will call all required modules to serve a web application
#

# Import all required  files/function
# flask is a 3rd party framework that serves web servlet that allows within a few lines create a web server
from flask import Flask
# Import the function register_blueprint from path routes/register.py
# This could be directly written in the main file, but, it is not recommended.
# We should always modularize our application
from routes.register import register_blueprint

# Create the Flask app from flask native library
app = Flask(__name__)


# Route for the home page
# This will create a path on our application
# if you go to http://localhost:5000/ it will serve this output ↓
# Welcome to Flask
# Change it and refresh your app to understand how it works
@app.route('/')
def home():
    return "Welcome to Flask!"

# This one is referenced by the import from the begging of this file
# It will create another route as we have above (from welcome to flask)
# check the file on routes/register.py to see what it does!
# if you need to create another route, mimic this behave to create another route
app.register_blueprint(register_blueprint)

# Run the app
# This a flask directive, in order to run the webserver, you need to run like this
if __name__ == '__main__':
    app.run(debug=True)
