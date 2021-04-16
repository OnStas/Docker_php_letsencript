import os
from pathlib import Path

p = os.path.abspath('compose-automation.py')
print(p)
path = Path(p).parent.parent
print(path)
try:
   os.system('mv compose-automation.py ' + str(path))
except:
   print('file not found')
print('..copy done...')
os.system('echo \"*/5 * * * * python ' + str(path) + '/compose-automation.py\" >> /etc/crontab')
# print('echo \"*/5 * * * * python ' + str(path) + '/compose-automation.py\" >> /etc/crontab')
