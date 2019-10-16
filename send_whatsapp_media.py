import os
from twilio.rest import Client

"""Don't forget to run source on twilio.env to
ensure the environment variables are loaded.
"""
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         body="I don't like spam!",
         status_callback='https://postb.in/1571036965860-1086896772030',
         to='whatsapp:+61406257985'
     )

print(message.sid)
print(message.media._uri)
