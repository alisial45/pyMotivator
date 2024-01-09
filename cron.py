from apscheduler.schedulers.background import BackgroundScheduler
from motivator import quote, send_message_to_whatsapp
from tzlocal import get_localzone
import time

tz = get_localzone()
scheduler = BackgroundScheduler(timezone='Asia/Karachi')
scheduler.start()

job = scheduler.add_job(send_message_to_whatsapp,'cron',[quote],hour=5,minute=3)

print(job)

while True:
    time.sleep(1)

    


