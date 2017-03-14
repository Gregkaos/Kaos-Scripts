#!/usr/bin/python
from scapy.all import *

# creates a single tcp packet with reserved bit (evil bit) set.   Use with Snort rule as heartbeat monitor

ip=IP(src="10.1.1.100", dst="10.1.1.1", flags=4, frag=0)
tcpsyn=TCP(sport=1500, dport=80, flags="S", seq=4096)
send(ip/tcpsyn)

'''
Snort Rule:
alert tcp 10.1.1.100 1500 -> 10.1.1.1 80 (msg:"Evil Bit detected"; fragbits:R+; sid:1000666;)
'''
