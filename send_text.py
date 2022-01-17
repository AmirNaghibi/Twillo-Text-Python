from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, twilio_cell

client = Client(account_sid, auth_token)

message = "Hello World! This message is sent using python and twilio SMS API!"

try:
    client.messages.create(to = my_cell, from_ = twilio_cell, body = message)
    print("Success!")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

