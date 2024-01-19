from apscheduler.schedulers.background import BackgroundScheduler
from motivator import quote #,send_message_to_whatsapp
from tzlocal import get_localzone
import time

def simple():
   print(quote)


tz = get_localzone()
scheduler = BackgroundScheduler(timezone='Asia/Karachi')
job = scheduler.add_job(simple,'interval', minutes=1)
scheduler.start()
print(job)

while True:
    time.sleep(1)


