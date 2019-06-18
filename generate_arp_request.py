#1/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    arp_broadcast = scapy.Ether()
    arp_broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = arp_broadcast/arp_request
    arp_request_broadcast.show()

    # to know about the fields which can be provided in scapy.ARP()
    # scapy.ls(scapy.ARP())
    print(arp_broadcast.summary())

scan("192.168.0.1/24")

