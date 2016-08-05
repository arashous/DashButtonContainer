# DashButtonContainer
A Dockerfile and script that makes it easy to run an environment for listening to Amazon Dash button communications


Got the original code from : https://gist.github.com/eob/a8b5632f23e75b311df2

The new version of the button behaves slightly differently and doesn't in the same manner. Modified code to listen to new button. This will listen for anything on the network.

from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    print "ARP Probe from: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)

This version will filter by MAC address of the button you have

from scapy.all import *
def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].hwsrc == 'c0:ff:ee:c0:ff:ee':
      print "You need coffee"
      print "Now you can do stuff"
    else:
      print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)

Build Container : 

docker build --tag "dashbuttonlistener:latest" ./DashButtonContainer/

Run Container : 

docker run --rm --network=host dashbuttonlistener:latest

