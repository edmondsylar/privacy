import pymysql
from time import sleep

data = []
for i in range(0, 25):
	data.append(i)

count =  len(data)

print (int(count))

def init_db_information_batch():
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='more')
		cur = conn.cursor()
		print ('connected, stroing record count.')
		sleep(2)

		sql = "INSERT INTO info (data) VALUES ('{}')".format(int(count))
		cur.execute(sql)
		conn.commit()
		cur.close()
		print ('Done stroing information, extraction NEXT.')
		# sleep(2)

		# exit()
		information_fill()
	except Exception as e:
		print (e)
		# print ('Problem connecting to database.')

	#Here call the next function.


def information_fill():
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='more')
		cur = conn.cursor()
		print ('connected, reading to send information to db')

		for val in data:
			sql = "INSERT INTO patner (data) VALUES ('{}')".format(i)
			cur.execute(sql)
			conn.commit()
			cur.close()

		print ('Done....')
		sleep(10)
		exit()
	except Exception as err:
		print (err)
		# print ('something went wrong.....')

init_db_information_batch()

