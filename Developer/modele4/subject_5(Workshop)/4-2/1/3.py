import vk_api
import datetime
import time
from mtok import tok


while True:
    token = tok
    session = vk_api.VkApi(token=token)

    delta = datetime.timedelta(hours=4, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)

    nowdata = t.strftime("%d.%m.%Y")
    nowtime = t.strftime("%H:%M")

    on = session.method("friends.getOnline")
    counted = len(on)

    # session.method("status.set", {'text': nowtime + " ● " + nowdata + " ● " + "Друзей онлайн: " + str(counted)})
    print(nowtime + " ● " + nowdata + " ● " + "Друзей онлайн: " + str(counted))
    time.sleep(5)
