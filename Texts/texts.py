from twilio.rest import TwilioRestClient
# import string
#
messagei = raw_input("Your message: ")

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC682d8688434bdbc55f0e2b6f77820bfa"
auth_token  = "a8102f65ee02ca45d29e1cbe20e5289d"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body = messagei,
    to="+19046555263",    # Replace with your phone number
    from_="+19045496907") # Replace with your Twilio number
print message.sid
