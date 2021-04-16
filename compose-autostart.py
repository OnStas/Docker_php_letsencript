import os
import requests

def ContainerManeger():
    print(' DEF Web site does not exist_ start CM')
    os.system('git clone https://github.com/OnStas/Docker_php_letsencript temp')
    os.system('mv temp/.git Docker_php_letsencript')
    os.system('rm -rf temp')
    os.system('docker system prune -y')
    os.system('docker-compose -f Docker_php_letsencript/docker-compose.yml up')


url = 'https://boxadi.com/'
try:
    x = requests.get('url')
except:# ConnectionError:
    print(' Web site does not exist1')
    ContainerManeger()
else:
    if x.ok:
        print(x.ok +' Web site exists')
    else:
         ContainerManeger()
         print(x.res + ' Web site does not exist2')
