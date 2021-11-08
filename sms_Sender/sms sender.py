from twilio.rest import Client
account_sid = 'paste acc sid here'
auth_token = 'paste auth token here '
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="you are hacked.",
                     from_='paste sender number ',
                     to="paste reciever number"
                 )

print(message.sid)
''' 
for reference go through this link :
    https: // youtu.be / M_dBtarTb8Y
'''