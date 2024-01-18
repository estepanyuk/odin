import vk_api
import datetime
import time
from mtok import tok

while True:
    token = tok
    vk_session = vk_api.VkApi(token=token)

    delta = datetime.timedelta(hours=4, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)

    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d:%m:Y")

    on = vk_session.method("friends.getOnline")
    couted = len(on)

    # выводим информацию в статус вк
    # vk_session.method("status.set", {"text":nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(couted)})
    # выводим в консоль
    print(nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(couted))
    time.sleep(5)
