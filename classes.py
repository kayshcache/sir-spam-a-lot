import http.client
import pprint
import json
import requests
import os

class TwilioClient:
    def __init__(self, account_sid=None, auth_token=None):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.URL = 'https://api.twilio.com/2010-04-01/Accounts/'
        self.URI = self.URL + account_sid + '/Messages.json'
        print(self.URI)
        print(self.account_sid)

    def post_message(self, _whatsapp, _body, _number):
        message_data = {
                'Body': _body,
                'From': 'whatsapp:+14155238886',
                'To': f'whatsapp:{_number}'}
        if _whatsapp == False:
            message_data['From'] = '+12162796757'
            message_data['To'] = _number
        response = requests.post(
                self.URI,
                data=message_data,
                auth=(self.account_sid, self.auth_token))
        print(response)


#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
# print(os.environ['TWILIO_ACCOUNT_SID'])

#twilio_client = TwilioClient(account_sid, auth_token)
#twilio_client.post_request()

def check_get_response(get_response_object):
    if get_response_object:
        print('Response OK')
    else:
        print('Fail, dude')


response = requests.get('https://api.twilio.com')
check_get_response(response)


#connection = http.client.HTTPSConnection('api.twilio.com')

def get_headers():
    connection.request('GET', '/')
    response = connection.getresponse()
    headers = response.getheaders()
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(f'Headers: {headers}')
    print(f'Status: {response.status} and reason: {response.reason}')

#get_headers()

def post_stuff():
    connection = http.client.HTTPSConnection('www.httpbin.org')
    headers = {'Content-type': 'application/json'}

    foo = {'text': 'Hello HTTP'}
    json_data = json.dumps(foo)

    connection.request('POST', '/post', json_data, headers)
    response = connection.getresponse()
    print(response.read().decode())

#post_stuff()
#connection.close()
