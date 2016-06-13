#!/usr/bin/env python
import socket

__author__ = "Dan Clegg"
__email___ = "nospamdan@gmail.com"
__maintainer__ = "Dan Clegg"
__status__ = "Production"
# http://danclegg.net
# @dgclegg

def parse(ip):
    # parse and validate ip address
    try:
        socket.inet_pton(socket.AF_INET,ip)
        return "valid"
    except socket.error, e:
        try:
            socket.inet_pton(socket.AF_INET6,ip)
            return "valid"
        except:
            print "ERROR: %s" % e
