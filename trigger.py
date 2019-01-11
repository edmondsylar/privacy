from Server.DataFetch.appfine import *
import schedule
import time

def job():
	main()

schedule.every(1).day.at("00:00").do(job)

#Note trigger start here
print ('Trigger started.....')
while True:
	#Start running the scheduled task.
	schedule.run_pending()
