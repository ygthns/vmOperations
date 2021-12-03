import requests
import json
import os
import subprocess as sp

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
hostname= person_dict['data']['hostname']
oldHostname = file_read('/etc/hostname')
isChanged = False
fileFlag = os.path.exists('/etc/hostname')

if (oldHostname != hostname):
    os.system('hostnamectl set-hostname {}'.format(hostname))
