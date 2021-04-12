import os
import time
import requests
from requests.exceptions import ConnectionError


def ContainerManeger():
    os.system('docker system prune -y')
    os.system('docker-compose up')


while True:
    url = 'https://boxadi.com/'
    try:
        x = requests.get('url')
    except:
        print('Web site does not exist1')
        ContainerManeger()
    else:
        if x.ok:
            print('Web site exists')
        else:
            ContainerManeger()
            print('Web site does not exist2')
    time.sleep(60)
