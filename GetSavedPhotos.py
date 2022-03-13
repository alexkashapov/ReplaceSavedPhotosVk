# coding=utf-8
import requests
import json

import vk_api

creds = open("creds.txt","r")
cred_arr = creds.readline().split(',')
login,password = cred_arr[0], cred_arr[1]
creds.close()
session = requests.Session()
vk_session=vk_api.VkApi(login,password)
ownerId = cred_arr[2]
fromAlbumId = cred_arr[3]
toAlbumId = cred_arr[4]
try:
    vk_session.auth(token_only=True)
    # vk_session.auth()
    vk = vk_session.get_api()
    for i in range(20):
        photos = json.dumps(vk.photos.get(owner_id = ownerId,album_id=fromAlbumId))
        photos_dict = json.loads(photos)
        countPhotos = photos_dict['count']
        print('Итерация ', i+1,  '\nОсталось фото: ',countPhotos)
        photos_list = photos_dict['items']
        for photo in photos_list:
            vk.photos.move(owner_id=ownerId, target_album_id=toAlbumId,photo_id=photo['id'])
    # photos_json = json.loads(photos_list)
    # print(type(photos_json))
except vk_api.AuthError as er_msg:
    print(er_msg)
