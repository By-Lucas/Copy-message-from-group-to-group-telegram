from telethon import TelegramClient, events, sync
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
import requests

# Remember to use your own values from my.telegram.org!
api_id = 2981443
api_hash = '98fc1e323ff55ff7198cf2ddd7039b93'

chat = '@tk_teste'

token = 'token do bot'
chat_id = -100 + 'id do chat'
texto = 'teste do bot'

phone = '55749'

client = TelegramClient('anon', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing in the client
    client.sign_in(phone, input('Digite seu código: '))
    client.sign_in(password, input('Digite sua senha se tiver'))
def send_mess():
    @client.on(events.NewMessage(chats=chat))
    async def my_event_handler(event):
        menssagem = event.raw_text
        print(f'Grupo: {chat} | Mensagem: {menssagem}')
        # receptor user_id e access_hash, use
        # meu user_id e access_hash para referência
        receiver = InputPeerUser(937809478, 7058533597106621900)

        #Enviar mensagem
        send_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={menssagem}")
        data = send_msg.json()
        #print(data)
send_mess()

client.start()
client.run_until_disconnected()