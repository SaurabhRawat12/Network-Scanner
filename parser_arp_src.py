#1/usr/bin/env python

import scapy.all as scapy
import optparse


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


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest="target", help="target ip address entry")
    (target, arguments) =  parser.parse_args()
    return target




    # to know about the fields which can be provided in scapy.ARP()
    # scapy.ls(scapy.ARP())
    # print(arp_broadcast.summary())
target_ip = get_arguments()
scan_result = scan(target_ip.target)
print_result(scan_result)

