import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

user = "AC923d3cd6c283d2d956b80225bdbf47db"
password = "e4332de2664c4bba54d6bf426b8c4d49"
client = Client(user, password)

try:
    message = client.messages.create(to="+19175998853", from_="+15555555555", body="Hello there!")

except TwilioRestException as e:
    print(e)

# logging
logging.basicConfig()
client.http_client.logger.setLevel(logging.INFO)