import os
import requests
import shutil
from download_utility import(download_file)

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_imag_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = https://cdn.britannica.com/65/161665-50-C4B1FA75/Waves-North-Shore-Oahu-Hawaiian-Islands.jpg
# for smallish item
#r = request.get(url, stream=True)
#r.raise_for_status() #200
#with open(downloaded_imag_path, 'wb') as f:
    #f.write(r.content)

#dl_file_name = os.path.basename(url)
#new_dl_path = os.path.join(DOWNLOAD_DIR, dl_file_name)
#with requests.get(url, stream=True) as r:
#    with open(new_dl_path, 'wb') as file_obj:
 #       shutil.copyfileobj(r.raw, file_obj)

download_file(url, DOWNLOAD_DIR)