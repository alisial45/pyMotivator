import requests
import os
from twilio_conn import send_message_to_client

def quote_of_the_day(category):

            
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'te2qR+FiRSs7ga6dCtDw3Q==9GrZ9Uc6MkZpX24x'})

    if response.status_code == requests.codes.ok:
          
        data = response.json()
        return data[0]['quote']
    else:
       # error ="Error {}".format(response.text)
        return  response.error

     
quote=quote_of_the_day(category='happiness')
send_message_to_client(quote)






        

