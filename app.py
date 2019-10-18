# /usr/bin/env python

import os
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
from classes import TwilioClient

app = Flask(__name__)

POSTBIN_ENDPOINT = ''
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
special_pic_one = os.environ['SPECIAL_ONE']
special_pic_two = os.environ['SPECIAL_TWO']

whatsapp = True
message_body = '~Spam~'
message_to = '+61406257985'
twilio_client = TwilioClient(account_sid, auth_token)
#twilio_client.post_message(True, message_body, message_to)

def give_me_form():
    form_html = '<form method="POST"><input name="text">' \
            '<input type="submit"></form>'
    return form_html

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
    html = '<h1>Hello from The Royal Court of Spamelot</h1>'
    html += '<a href="whatsapp://send?phone=+14155238886' \
            '&text=scientific-parallel">Follow this link on your phone</a>'
    html += give_me_form()
    messages = client.messages.list(limit=20)
    list_items = map(lambda record:
            f'<li>{record.sid}: {record.status}</li>',
            messages)
    list_items = ''.join(list_items)
    html += f'<h2>The last 20 messages sent through this service</h2>' \
            f'<ol>{list_items}</ol>'
    return html

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/webhook', methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a receipt SMS."""
    # Start our response
    resp = MessagingResponse()
    message = Message()
    message.media(special_pic_two)
    message.body('_spam_ is, therefore _I_ am.')
    resp.append(message)
    return str(resp)

if __name__ == '__main__':
  app.run(debug=True)
