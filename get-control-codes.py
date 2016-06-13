#!/usr/bin/env python
import argparse
import json
import requests
import sys
import validateIp

parser = argparse.ArgumentParser(description='Get Control Codes for a Sony Display')
parser.add_argument('--ip')

args = parser.parse_args()

# parse and validate ip address
if args.ip:
    try:
        ipValidation = validateIp.parse(args.ip)
        assert(ipValidation == "valid")
        ip = args.ip
    except:
        sys.exit("--ip is not a proper IP address")
else:
    sys.exit("--ip is a required argument")

requestUrl = "http://%s/sony/system" % ip
body = {"method":"getRemoteControllerInfo","params":[],"id":10,"version":"1.0"}
response = requests.post(requestUrl, json=body)
print response.json()
#return response.json()
