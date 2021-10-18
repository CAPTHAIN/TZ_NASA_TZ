import requests
import json
import os
from datetime import date as d
from datetime import timedelta

from django.core.files import File

from .models import *


def get_post_data():
    api_key = 'Yq5Y97tgETWEzqGPY9Z7c6caiW4KhCtTYL0zZJvz'
    date = d.today()

    if Post.objects.all():
        c = 1
    else:
        c = 14

    def download_image(url, date):
        if os.path.isfile(f'{date}.png') == False:
            raw_image = requests.get(url).content
            with open(f'nasa/media/{date}.jpg', 'wb') as file:
                file.write(raw_image)
        else:
            return FileExistsError

    while c > 0:
        c -= 1

        raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}').text
        response = json.loads(raw_response)
        title = response['title']

        if not Post.objects.filter(title=title):
            text = response['explanation']
            date_out = response['date']
            media_type = response['media_type']

            new_post = Post(title=title, text=text, date=date_out)
            if media_type == 'image':
                download_image(response['url'], date_out)
                new_post.photo.save(f"{date_out}.jpg", File(open(f"nasa/media/{date_out}.jpg", "rb")))
            else:
                new_post.save()

        date -= timedelta(days=1)