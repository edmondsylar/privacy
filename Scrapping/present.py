from appfine import *
import schedule
import time 

def job():
	main()

schedule.every(10).minutes.do(job)

print ('Triggered 10 minutes.')
while True:
	schedule.run_pending()
	# Run the pending task.