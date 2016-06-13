#!/usr/bin/env python
import socket

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
