import requests
import json
import os
import subprocess as sp
from hashlib import sha256

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


uuid = sp.getoutput('/usr/sbin/dmidecode -s system-uuid') #uuid of the vm assigned to uuid variable
response = requests.get('https://api.plusclouds.com/v2/iaas/virtual-machines/meta-data?uuid={}'.format(uuid)) #requests the information of the instance
person_dict = response.json() #json to dict
password= person_dict['data']['password']
readablePassword = password
password = sha256(readablePassword.encode()).hexdigest()
isChanged = False
fileFlag = os.path.exists('/var/log/passwordlogs.txt')

if (fileFlag == True):
    oldPassword = file_read('/var/log/passwordlogs.txt')
    if (oldPassword != password):
        isChanged= True
        print('Password has been changed in while ago')
        f = open("/var/log/passwordlogs.txt", "w+")
        f.write(password)
        f.close()
    else:
        print('Password has not been changed')
else:
    isChanged= True
    f = open("/var/log/passwordlogs.txt", "w+")
    f.write(password)
    f.close()

if (isChanged == True):
    cmd = "bash -c \"echo -e '{}\\n{}' | passwd root\"".format(readablePassword, readablePassword)
    sp.check_call(cmd, shell=True)
    print('Password has been updated successfully')
