from twilio.rest import Client
import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR) + '/.env')

def get_token():
    
    with open("env.txt", "r") as f:
        return f.read()

def send_sms(number, mess):
    num = number
    account_sid = "ACa59320f2dad74cafe284fd22f01f7476"
    auth_tok = env("auth_token")
    
    #auth_token = auth_tok[14:-1]
    
    client = Client(account_sid, auth_tok)

    message = client.messages.create(
    body= mess,
    from_='[+][1][9388882655]',
    to='[+][234][%s]' %num
    )
    #print(message.sid)
    