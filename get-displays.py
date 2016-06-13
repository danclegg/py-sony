#!/usr/bin/env python
import argparse
import nmap
import sys
import validateIp

__author__ = "Dan Clegg"
__email___ = "nospamdan@gmail.com"
__maintainer__ = "Dan Clegg"
__status__ = "Development"
# http://danclegg.net
# @dgclegg

parser = argparse.ArgumentParser(description='Get Sony Devices in address range')
parser.add_argument('--ip')
parser.add_argument('--subnet')

args = parser.parse_args()

subnet = None
ip = None

if not args.ip and not args.subnet:
    sys.exit("--ip or --subnet must be specified")

# parse and validate ip address
if args.ip:
    try:
        subnet = None
        ipValidation = validateIp.parse(args.ip)
        assert(ipValidation == "valid")
        ip = args.ip
    except:
        sys.exit("--ip is not a proper IP address")

if args.subnet:
    try:
        ip = None
        subnetValidation = validateIp.parse(args.subnet)
        assert(subnetValidation == "valid")
        subnet = args.subnet
    except:
        sys.exit("--subnet is not a proper format")

nm = nmap.PortScanner()

if subnet is None:
    try:
        nm.scan(ip, arguments='-O')
    except:
        sys.exit("Error scanning IP")
elif ip is None:
    try:
        cidr = subnet + "/24"
        nm.scan(cidr, arguments='-O')
    except:
        sys.exit("Error scanning subnet")
else:
    sys.exit("Error getting device info")


hosts_to_check = []
sonys = []

#find devices with mac addresses and output to the hosts_to_check array
for h in nm.all_hosts():
    if 'mac' in nm[h]['addresses']:
        hosts_to_check.append(nm[h]['addresses'])

#find sony devices in hosts_to_check array and output ips to the sonys array
for host in hosts_to_check:
    if host['mac'].find("AC:9B:0A") == 0:
        sonys.append(host['ipv4'])

print sonys
