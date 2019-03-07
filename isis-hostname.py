import sys
import xml.etree.ElementTree as ET
import re

XML_ISIS_HOSTNAME = "/home/lpolak/isis_hostname/isis_hostname.xml"

#Juniper XML Namespace
NS = {'junos':'http://xml.juniper.net/junos/15.1F6/junos-routing' }
OUTPUT = '/home/lpolak/isis_hostname/host_ip.txt'

tree = ET.parse(XML_ISIS_HOSTNAME)
root = tree.getroot()

hosts = {}

'''
Function converting ISIS system ID to IPv4 address
e.g. '0621.7912.8001' will be converted to 62.179.128.1
'''
def convert_sysid_to_ip(sys_id):
    first_oct = int(sys_id[0:3])
    second_oct = int(sys_id[3] + sys_id[5:7])
    third_oct = int(sys_id[7:9]+ sys_id[10])
    fourth_oct = int(sys_id[11:])
    ip_address =  str(first_oct)+'.'+str(second_oct)+'.'+str(third_oct)+'.'+str(fourth_oct)
    return ip_address

'''
Function remove re0/re1 Junos identifier from the hostname
'''
def cleanup_hostname(hostname):
    if re.match('[Rr][Ee][01]-(.*)',hostname):
        hostname = re.sub('[Rr][Ee][01]-(.*)','\g<1>',hostname)
    elif re.match('(.*-.*-.*)-[Rr][Ee][01]',hostname):
        hostname = re.sub('(.*-.*-.*)-[Rr][Ee][01]', '\g<1>', hostname)
    return hostname

for host in root.findall('.//junos:isis-hostname',NS):
    hostname = cleanup_hostname(host.find('junos:system-name',NS).text)
    sys_id = host.find('junos:system-id', NS).text
    hosts[hostname]= convert_sysid_to_ip(sys_id)

if hosts:
    with open(OUTPUT,'w') as file:
        for key in hosts.keys():
            file.write(key + ' ' + hosts[key] + '\n')
else:
    sys.stderr.write('Error. Host list is empty\n')
