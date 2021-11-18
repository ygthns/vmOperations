import platform
import distro
import os
import subprocess as sp
import requests
from hashlib import sha256
import urllib.request

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

if platform.system()=='Linux':
    distroName= str(distro.linux_distribution(full_distribution_name=False)[0]) + '_' + str(distro.linux_distribution(full_distribution_name=False)[1])
    print(distroName)
    uuid = sp.getoutput('/usr/sbin/dmidecode -s system-uuid') #uuid of the vm assigned to uuid variable
    response = requests.get('http://10.100.0.25/v2/iaas/virtual-machines/meta-data?uuid={}'.format(uuid)) #requests the information of the instance
    person_dict = response.json() #json to dict
    oldDisk='0'
    total_disk= person_dict['data']['virtualDisks']['data'][0]['total_disk']
    total_disk=str(total_disk)
    hostname= person_dict['data']['hostname']
    password= person_dict['data']['password']
    readablePassword = password
    password = sha256(''.encode()).hexdigest()

    #Password
    fileFlag = os.path.exists('/var/log/passwordlogs.txt')
    if (fileFlag == True):
        oldPassword = file_read('/var/log/passwordlogs.txt')
        if (oldPassword != password):
            print('run hostname.py')
    else:
        print('run hostname.py')


    #Hostname
    oldHostname = file_read('/etc/hostname')
    if oldHostname != hostname:
        print('run hostname.py')

    
    #Storage
    isDiskLog = os.path.exists('/var/log/disklogs.txt')
    if (isDiskLog==True):
        oldDisk = file_read('/var/log/disklogs.txt')
        if oldDisk != total_disk:
            print('run storage.py')
        if os.path.exists("/var/log/isExtended.txt") == True:
            isExtended = file_read("/var/log/isExtended.txt")
            if isExtended  == 1:
                print('run storage.py')
    else:
        print('run storage.py')

#Windows
if platform.system()=='Windows':
    distroName = str(platform.system()) + '_' + str(platform.release())



#ssh_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCqql6MzstZYh1TmWWv11q5O3pISj2ZFl9HgH1JLknLLx44+tXfJ7mIrKNxOOwxIxvcBF8PXSYvobFYEZjGIVCEAjrUzLiIxbyCoxVyle7Q+bqgZ8SeeM8wzytsY+dVGcBxF6N4JS+zVk5eMcV385gG3Y6ON3EG112n6d+SMXY0OEBIcO6x+PnUSGHrSgpBgX7Ks1r7xqFa7heJLLt2wWwkARptX7udSq05paBhcpB0pHtA1Rfz3K2B+ZVIpSDfki9UVKzT8JUmwW6NNzSgxUfQHGwnW7kj4jp4AT0VZk3ADw497M2G/12N0PPB5CnhHf7ovgy6nL1ikrygTKRFmNZISvAcywB9GVqNAVE+ZHDSCuURNsAInVzgYo9xgJDW8wUw2o8U77+xiFxgI5QSZX3Iq7YLMgeksaO4rBJEa54k8m5wEiEE1nUhLuJ0X/vh2xPff6SQ1BL/zkOhvJCACK6Vb15mDOeCSq54Cr7kvS46itMosi/uS66+PujOO+xt/2FWYepz6ZlN70bRly57Q06J+ZJoc9FfBCbCyYH7U/ASsmY095ywPsBo1XQ9PqhnN1/YOorJ068foQDNVpm146mUpILVxmq41Cj55YKHEazXGsdBIbXWhcrRf4G2fJLRcGUr9q8/lERo9oxRm5JFX6TCmj6kmiFqv+Ow9gI0x8GvaQ== username@hostname'
#auth_ssh_call='echo "{}" >> ~/.ssh/authorized_keys'.format(ssh_key)
#os.system(auth_ssh_call)