from app import *
from controllers import *

# Creata an object intance of the dbMode in controllers
client = dbModel()

# Create Default route.
@app.route('/')
def index():
    make_request = client.default()
    return make_request

#Create file fetch route
@app.route('/file')
def file_get():
    get = client.data_load()
    return get
