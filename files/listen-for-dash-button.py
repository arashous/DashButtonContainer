
from scapy.all import *
from time import strftime

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    print "{0} - ARP Probe from device: {1}".format(strftime("%Y%m%d-%H%M%S"), pkt[ARP].hwsrc)

print sniff(prn=arp_display, filter="arp", store=0, count=10)
