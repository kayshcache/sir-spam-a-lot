# /usr/bin/env python

import os
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

POSTBIN_ENDPOINT = ''
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
special_pic_one = os.environ['SPECIAL_ONE']
special_pic_two = os.environ['SPECIAL_TWO']

def send_whatsapp_media():
    message = client.messages \
    .create(
         media_url=[special_pic_one],
         from_='whatsapp:+14155238886',
         body="I don't like spam!",
         status_callback=POSTBIN_ENDPOINT,
         to='whatsapp:+61406257985'
     )

@app.route('/')
def display_homepage():
    html = '<h1>Hello, from Greenwich Village Accommodation, North Shore</h1>'
    html += '<a href="whatsapp://send?phone=+14155238886&text=scientific-parallel">Follow this link on your phone</a>'
    messages = client.messages.list(limit=20)
    html += '<h2>The last 20 messages sent through this service</h2><ol>'
    for record in messages:
        html += f'<li>{str(record)[1:-1]}</li>'
    html += '</ol>'
    return html

@app.route('/sms', methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a receipt SMS."""
    # Start our response
    resp = MessagingResponse()
    message = Message()
    message.media(special_pic_two)
    message.body('Spam ahoy!')
    resp.append(message)
    return str(resp)

if __name__ == '__main__':
  app.run(debug=True)
