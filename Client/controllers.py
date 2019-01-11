# Please note and remember to use redirect
import csv
import datetime
import pymysql
from verified import *
import requests
import jwt
from flask import flash

connection = {
    'host':'localhost',
    'user':'root',
    'passwd':None,
    'database':'astuteclient'
}

# client_trial

class dbModel:
    def __init__(self):
        self.conn = pymysql.connect(**connection)
        self.cur =  self.conn.cursor()
        self.licence = '5c1f87c380f2b9.90994146'
        self.clientID = '5c1f54de2b5217.19046714'


    def data_load(self, token):
        name = 'dumps'
        load_sql = """LOAD DATA LOCAL INFILE '{}.csv' INTO TABLE astuteclient.tabular    \
         FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;""".format(name)
        host = 'localhost'
        user = 'root'
        password = None
        csv_to_mysql(load_sql, host, user, password)

        return self.mgs()


    def mgs(self):
        return jsonify({'msg':'The  operation completed Succuessfully'})

    def default(self):
        lic = self.licence
        cli = self.clientID
        try:
            resp = requests.get('http://127.0.0.1:8080/request/{}/{}'.format(self.clientID, self.licence))
            result = resp.content
            token = result
            return self.protected_route_for_execution(token)
            # return ('{}'.format(token   ))
        except Exception as exp:
            return (exp)


    def protected_route_for_execution(self, arg):
        # got = arg
        try:
            print ('argument is {}'.format(arg))
            col = jwt.decode(arg, 'secret', algorithms='HS256')
            return self.create_file(arg)

        except Exception as err:
            return ('{}'.format(err))

    def create_file(self, arg):
        # decoded = jwt.decode(arg, 'secret', options=options)
        # return (arg)
        try:
            file_request = requests.get('http://127.0.0.1:8080/uploads/%s/filename' % arg)
            open('received.csv', 'wb').write(file_request.content)
            return ('Updates ready for extraction.')
            # return ('{}'.format(file_request.content))
        except Exception as erp:
            return ('Client Side {}'.format(erp))
