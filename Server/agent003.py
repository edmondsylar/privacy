from flask import Flask
app = Flask(__name__, static_url_path='') #Create a flask application here.
app.config['UPLOAD_FOLDER'] = ''

# Now import all views
from views import *


if __name__ == "__main__":
    app.run(debug=True, port=8080)
