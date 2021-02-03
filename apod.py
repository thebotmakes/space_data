import requests
import time
import json
import os
from PIL import Image
from IPython.display import display
from datetime import date

today = date.today()
my_api='oWUfgkRloUBUu6IyidikTOxs3JNa9OqPd5rbHxGE'

def get_apod_data(api_key):
    raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
    response = json.loads(raw_response)
    return response

def download_image(url, date):
    if os.path.isfile(f'{date}.png') == False:
        raw_image = requests.get(url).content
        with open(f'{date}.jpg', 'wb') as file:
            file.write(raw_image)
            
    else:
        return FileExistsError
    
apod_data = get_apod_data(my_api)
download_image(apod_data['url'], apod_data['date'])
if apod_data['media_type'] == 'video':
    pass
else:
    file_name = apod_data['date'] + '.jpg'
    apod_img = Image.open(file_name)
    apod_img.save(r'apod.jpg')