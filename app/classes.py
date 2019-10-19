import json
import requests

class TwilioClient:
    """Class for making HTTP requests to Twilio REST API
    
    This class is for managing the communication between
    the Flask app and the Twilio API.
    
    Attributes:
        account_sid: SID specific to the account being used,
        also retrieved from environment.
        auth_token: Private token passcode scooped out of
        environment variable.
        URL: Twilio main public endpoint for any account.
        URI: URL + account_sid and '/Messages.json' to make
        the authenticated endpoint.

    Methods:
        post_message:
    """
    def __init__(self, account_sid=None, auth_token=None):
        """Inits TwilioClient class with params."""
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.URL = 'https://api.twilio.com/2010-04-01/Accounts/'
        self.URI = self.URL + account_sid + '/Messages.json'
        self.WHATSAPP_SANDBOX_NUM = 'whatsapp:+14155238886'
        self.SMS_NUM = '+12162796757'

    def post_message(self, message_data):
        """Method for POST requests to Twilio endpoint

        Args:
            whatsapp: Boolean indicating whether or not use WhatsApp - this
                class can be used for SMS - simply make call this method
                with False as the first argument.
            body: String of the body text
            number: String E167 number formatted internation phone number
            message_data: Dictionary containing body, from, to, and a URL
                image media if required.

        Returns:
            response: The object returned by Twilio REST API is a
            JSON to dictionary object.
            
        """
        message_data['From'] = self.SMS_NUM
        if message_data['WhatsApp'] == True:
            message_data['From'] = self.WHATSAPP_SANDBOX_NUM
            message_data['To'] = f"whatsapp:{message_data['To']}"
        response = requests.post(
                self.URI,
                data=message_data,
                auth=(self.account_sid, self.auth_token))
        return response


class HtmlCssBuilder:
    """Class for producing bits of HTML & CSS"""
    def __init__(self):
        pass


class MessageHandler:
    """Class for generating messages of all kinds"""
    def __init__(self):
        pass

