from flask import Flask, request, url_for, request
# create a flask app.
app = Flask(__name__)

# Import the views from here.
from views import *

# Run the flask application.
if __name__=='__main__':
    app.config['SECRET_KEY'] = 'tasmanian_devil'
    app.run(debug=True)
