from datetime import datetime
from time import sleep
from config import text, filename, login, password

import requests
import vk_api

vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

working = True


def post_vk(post):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    sent_every_time = 7200 # можете поставить каждый час или каждые два часа

    upload_url = vk.photos.getWallUploadServer(group_id=217316654)['upload_url']

    response = requests.post(upload_url, files={'file': open(filename, 'rb')}).json()

    data_photo = vk.photos.saveWallPhoto(
        group_id=217316654,
        server=response['server'],
        photo=response['photo'],
        hash=response['hash'])

    id_photo = f"photo{data_photo[0]['owner_id']}_{data_photo[0]['id']}"

    vk.wall.post(owner_id=-217316654, message=text, attachments=id_photo)
    sleep(sent_every_time)


while working:
    post_vk(text)
