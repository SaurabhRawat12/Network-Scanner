#1/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip
    arp_broadcast = scapy.Ether()
    arp_broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = arp_broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for elements in answered:
        clients_dict = {"ip": elements[1].psrc, "Mac Address": elements[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def print_result(result_list):
    print("IP Address\t\t\tMAC Address\n------------------------------------------------")
    for clients in result_list:
        print(clients["ip"] + "\t\t" + clients["Mac Address"])







    # to know about the fields which can be provided in scapy.ARP()
    # scapy.ls(scapy.ARP())
    # print(arp_broadcast.summary())

scan_result = scan("192.168.0.1/24")
print_result(scan_result)

