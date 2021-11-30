import os
import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# store credentials as environmental variables
account = os.environ["TWILIO_ACCOUNT_SID"]
token = os.environ["TWILIO_AUTH_TOKEN"]

# initialize Client with default params
client = Client()

# requires registered phone number with Twilio paid account
try:
    message = client.messages.create(to="+19175998853", from_="+15555555555", body="Hello there!")

except TwilioRestException as e:
    print(e)

# logging enabled
logging.basicConfig()
client.http_client.logger.setLevel(logging.INFO)