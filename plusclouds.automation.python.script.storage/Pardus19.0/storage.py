import requests
import json
import os
import subprocess as sp
import shutil
import fnmatch



#This function takes filename as input, and then read it and return as a string variable
def file_read(fname):
        with open (fname, "r") as myfile:
                data = myfile.readlines()
                #empty string created in order to make list variable str.
                str1 = ""  
                # traverse in the string  
                for ele in data: 
                    str1 += ele  
                return str1
def extend_disk():
    try:
        cmd = "bash -c \"echo -e 'd\n\nn\n\n\n\n\nw\n' | sudo fdisk /dev/xvda\""
        sp.check_call(cmd, shell=True)
    except Exception:
        pass
    file = open("/var/log/isExtended.txt", "w+")
    file.write('1')
    file.close()
    print("System will be rebooted.")
    os.system('sudo reboot')

xvdaCount = len(fnmatch.filter(os.listdir('/dev'), 'xvda*'))
xvdaCount=str(xvdaCount-1)
resizeCall='sudo resize2fs /dev/xvda{}'.format(xvdaCount)
total, used, free = shutil.disk_usage("/")
uuid = sp.getoutput('/usr/sbin/dmidecode -s system-uuid') #uuid of the vm assigned to uuid variable
try:
    response = requests.get('https://api.plusclouds.com/v2/iaas/virtual-machines/meta-data?uuid={}'.format(uuid),timeout=5)
except requests.exceptions.RequestException as e:  
    raise SystemExit(e)
person_dict = response.json() #json to dict
total_disk= person_dict['data']['virtualDisks']['data'][0]['total_disk']
total_disk=str(total_disk)
oldDisk='0'

isDiskLog = os.path.exists('/var/log/disklogs.txt')
if (isDiskLog==True):
    oldDisk = file_read('/var/log/disklogs.txt')
    f = open("/var/log/disklogs.txt", "w+")
    f.write(total_disk)
    f.close()
else:
    f = open("/var/log/disklogs.txt", "w+")
    f.write(total_disk)
    f.close()

isExtended = os.path.exists('/var/log/isExtended.txt')
if (total_disk != '10240'):
    if (isExtended == False):
            extend_disk()

    else:
        oldDisk = file_read('/var/log/disklogs.txt')
        if (oldDisk != total_disk):
            f = open("/var/log/disklogs.txt", "w+")
            f.write(total_disk)
            f.close()
            extend_disk()
else:
    print('No need for disk extend.')
    file = open("/var/log/isExtended.txt", "w+")
    file.write('0')
    file.close()

isExtended = file_read("/var/log/isExtended.txt")
if (isExtended == '1'):
    file = open("/var/log/isExtended.txt", "w+")
    file.write('0')
    file.close()
    os.system(resizeCall)
