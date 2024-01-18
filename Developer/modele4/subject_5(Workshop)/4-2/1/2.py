import vk_api
from mtok import tok

token = tok
session = vk_api.VkApi(token=token)
vk = session.get_api()

def send(msg):
    vk.messages.send(user_id=67885509, message=msg, random_id=0)

message = ""
while message != "exit":
    message = input()
    if message != "exit":
        send(message)


