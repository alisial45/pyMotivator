from twilio.rest import Client
from config import account_sid,auth_token,phone_no


def send_message_to_client(message):

 client = Client(account_sid, auth_token)
 message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to='whatsapp:{}'.format(phone_no)
              )
 return  message

