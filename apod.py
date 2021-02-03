# first we import all the libraries we need

import requests
import time
import json
import os
from PIL import Image
from IPython.display import display
from datetime import date

my_api='YOUR API KEY HERE' #replace the bit in the quotes with the API key you get by signing up at https://api.nasa.gov

# the next two functions are taken straight from NASA's API guide - just an amazing resource! The first one gets the json data, the second gets the image.

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
    
apod_data = get_apod_data(my_api) # use the first function to get the associated data for the picture (we only use the explanation and media type here)
download_image(apod_data['url'], apod_data['date']) # use the second function to get the image

if apod_data['media_type'] == 'video': 
    pass # this is a catch so we don't get errors if the file type is a video instead of a picture
else:
    with open("apod.txt", "w") as text_file:
        print(apod_data['explanation'], file=text_file) # this writes the 'explanation' field from the json data into a text file called apod.txt 
    file_name = apod_data['date'] + '.jpg'
    apod_img = Image.open(file_name)
    apod_img.save(r'apod.jpg') # these three lines open the image and save it as a jpg file
    
