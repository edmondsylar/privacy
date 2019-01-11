import pymysql 


foreing_uids = []
uids = []

def get_uid():
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='more')
		cur = conn.cursor()

		sql = "SELECT info_uid FROM info"
		cur.execute(sql)
		data = cur.fetchall()
		for each in data:
			for each in each:
				# print (str(each))
				foreing_uids.append(each)
		print ('\n\nThese are the foreign UIDs \n {}'.format(foreing_uids))
		print (' \n This is the last one in the list \n {}'.format(foreing_uids[-1]))
		uids.append(foreing_uids[-1])
		conn.close()
		cur.close()
		use_uid()


	except Exception as e:
		print (e)


def use_uid():
	try:
		coma = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='more')
		cur = coma.cursor()

		uid = uids[0]
		sql = "INSERT INTO patner (info_uid, data) VALUES ('{}', '{}')".format(uid, len(foreing_uids))
		print (uid)
		print (uids)
		cur.execute(sql)
		coma.commit()

		print ('Success')


	except Exception as e:
		print (e)

	cur.close()

while True:
	get_uid()