from twilio.rest import Client
from config import account_sid,auth_token,phone_no,twilio_no


def send_message_to_whatsapp(message):

 client = Client(account_sid, auth_token)
 
 message = client.messages.create(
            from_='whatsapp:{}'.format(twilio_no),
            body=message,
            to='whatsapp:{}'.format(phone_no)
              )
 
 return  message


