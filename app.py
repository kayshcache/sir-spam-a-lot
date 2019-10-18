# /usr/bin/env python

import os
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from twilio.rest import Client
from classes import TwilioClient

app = Flask(__name__)

POSTBIN_ENDPOINT = 'https://postb.in/1571411865319-0266059697605'

"""Global Constants"""
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_twilio_client = TwilioClient(account_sid, auth_token)# My handmade client class
client = Client(account_sid, auth_token) # Does same and more, from Twilio REST API Package
special_pic_one = os.environ['SPECIAL_ONE']
special_pic_two = os.environ['SPECIAL_TWO']

def give_me_form():
    """Function for making the form
    
    Returns:
        String - HTML and CSS
    
    """
    style_html = '<style>input' \
            '{width: 100%; max-width: 500px; box-sizing: border-box;' \
            'display: block; margin: 0; height: 60px; line-height: 60px;' \
            'font-size: 20px; border: 3px solid pink;}' \
            '</style>'
    form_html = '<form method="POST"><input class="form-input" name="text"' \
            'placeholder="E164 formatted phone number, eg. +61400666666">' \
            '<input type="submit"></form>'
    return style_html + form_html

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
def post_form():
    phone = request.form['text']
    message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body='Hi Joe! Thanks for placing an order with us.' \
                 ' We’ll let you know once your order has been' \
                 ' processed and delivered. Your order number is O12235234',
         to=f'whatsapp:{phone}'
     )
    message_status_output = f'Status for message SID: {message.sid}\n', \
            f'Delivery status: {message.status}\n' \
            f'Any errors: {message.error_code}'
    return message.sid

@app.route('/webhook', methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a receipt SMS."""
    # Start our response
    resp = MessagingResponse()
    message = Message()
    message.media(special_pic_two)
    message.body('_Spam_ is, therefore _I_ am.')
    resp.append(message)
    return str(resp)

@app.route('/whatsapp')
def show_form_for_whatsapp():
    return give_me_form()

@app.route('/whatsapp', methods=['GET', 'POST'])
def send_whatsapp_message():
    message_body = '~Spam~'
    message_data = {
        'WhatsApp': True,
        'Body': message_body,
        'To': request.form['text'],
        }
    response = my_twilio_client.post_message(message_data)
    return f'<p>Spam has been dutifully sent to</p>'

@app.route('/whatsapp-media')
def show_form_for_whatsapp_media():
    return give_me_form()

@app.route('/whatsapp-media', methods=['GET', 'POST'])
def send_whatsapp_media():
    phone = request.form['text']
    message = client.messages \
    .create(
         media_url=[special_pic_one],
         from_='whatsapp:+14155238886',
         body="I don't like spam!",
         status_callback=POSTBIN_ENDPOINT,
         to='whatsapp:{phone}'
     )
    return message.status

if __name__ == '__main__':
  app.run(debug=True)
