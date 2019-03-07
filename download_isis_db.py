#!/usr/bin/env python

import getpass
import paramiko
import sys
from ssh_credentials import USER,PASSWORD
dev = 'HOSTNAME'

OUTPUT_FILE = '/home/lpolak/isis_hostname/isis_hostname.xml'
user = USER 
passw = PASSWORD

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=dev,username=user,password=passw,allow_agent=False,look_for_keys=False)

stdin , stdout, stderr = ssh_client.exec_command('show isis hostname | display xml | no-more')
output = stdout.read()

ssh_client.close()

with open(OUTPUT_FILE,'w') as file:
    file.write(output)
