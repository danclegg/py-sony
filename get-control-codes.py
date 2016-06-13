#!/usr/bin/env python
import argparse
import json
import requests
import socket
import sys

parser = argparse.ArgumentParser(description='Get Control Codes for a Sony Display')
parser.add_argument('--ip')

args = parser.parse_args()

# parse and validate ip address
if args.ip:
    try:
        socket.inet_pton(socket.AF_INET,args.ip)
        print("IP address is valid")
        ip=args.ip
    except socket.error:
        sys.exit("--ip is not a proper IP address")
else:
    sys.exit("--ip is a required argument")
