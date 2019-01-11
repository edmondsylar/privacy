from flask import jsonify,make_response, send_from_directory
from agent003 import app
import re
from controllers import *
import jwt


test = UserModel()
@app.route('/security')
def index():
    return ('This is a security recovery route')


@app.route('/request/<client>/<license>')
def request_permision(client, license):
    checker = test.credentials_cheker(client, license)
    return checker


@app.route('/file_uploader/<filename>')
def send_file(filename):
    return ('This uplodas the file {}'.format(filename))

@app.route('/')
def indexer():
    return ('Astute Server')


@app.route('/error')
def error():
    return ('The Validator ran into a problem.')

@app.route('/uploads/<path:token>/<path:filename>')
def download_file(token, filename):
    filename = 'dumps.csv'
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename, as_attachment=True)
    except Exception as err:
        return ('Server side {}'.format(err))
