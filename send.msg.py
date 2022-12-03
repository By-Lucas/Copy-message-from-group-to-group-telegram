import requests

token = 'token do bot'
chat_id = -100 + 'id do grupo'
texto = 'teste do bot'

update = requests.get(f'https://api.telegram.org/bot{token}/getUpdates').json()
print(update)

send_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}").json()
print(send_msg)

# telegram url
url = f"https://api.telegram.org/bot{token}"

def send_mess():
    params = {'chat_id':chat_id, 'text': texto}
    response = requests.post(url + 'sendMessage', data=params)
    #return response


send_mess() 