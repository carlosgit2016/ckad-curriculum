from twilio.rest import Client
import os

def run():
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token  = os.environ.get('AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ.get('TO'), 
        from_=os.environ.get('FROM'),
        body=os.environ.get('MESSAGE'))
    
    print(message)
    
if __name__ == "__main__":
    run()