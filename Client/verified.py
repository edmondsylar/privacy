import pymysql
import pandas as pd
import sys
from flask import jsonify

# This is the file that does the actuall execution of the command to pick the data

def csv_to_mysql(load_sql, host, user, password):
    try:
        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)
        print('Connected to DB: {}'.format(host))
        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(load_sql)
        con.close()
        return jsonify({'Success':'Succuessfully loaded the table from csv.'})


    except Exception as e:
        return ('Error: {}'.format(str(e)))
        # sys.exit(1)
