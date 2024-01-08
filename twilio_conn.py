from twilio.rest import Client
import os

def send_message_to_client(message):

 account_sid =os.environ['TWILIO_ACCOUNT_ID']
 auth_token = os.environ['TWILIO_ACCESS_TOKEN']
 phone_no = os.environ['PHONE_NO']

 client = Client(account_sid, auth_token)
 message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to='whatsapp:{}'.format(phone_no)
              )



