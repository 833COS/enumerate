#!/usr/bin/python
# DOC ###################################################################
# enumerate
# create a list of every IP address within a given range
# Usage: 		enumerate [-r] network [network]
# Arguments:	-r		Randomize the resulting IPs
# Purpose:		
# 		Expand a network specification into a list of IP addresses.
# 		The network specification can be in any of the following formats:
#			###.###.###.###/SS		- CIDR (PREFERRED)
#			###.###.AA-BBB			- Range of IP addresses
#			###.###.###.*			- Wildcarded octet
# #######################################################################



import sys		# cmd line arguments
import random	# randomize the list of generated IPs
import math		# position of the ip ip/network argument.  Depends on rando.

ip = []
ipList = []
rando = 0
arg = 1



#-------------------------------------FUNCTIONS----------------------------

# Usage
def usage():
	print ""
	print "Usage: "
	print "\texpand_net [-r] network [network . . .]"
	print "\t-r \t- randomize IP address order"
	print "\tNetwork can be in any of the following formats:"
	print "\t ###.###.###.###/SS	- CIDR (PREFERRED)"
	print "\t ###.###.###.AA-BBB	- range of IP addresses"
	print "\t ###.###.###.*			- wildcarded octet"
	print ""
	quit()
	
	
	
# display the current IP address to STD Out
def showIP(a,b,c,d):
	newIP = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
	print newIP

	
# Increment to the next IP address and return items
def incrementIP(a,b,c,d):
	d += 1
	if d == 256:
		d = 0
		c += 1
		if c == 256:
			c = 0
			b += 1
			if b == 256:
				b = 0
				a += 1
				if a == 256:
					print ""
					print "ERROR:\tInvalid IP range generated."
					print "First octet exceeded 255."
					print ""
					quit()
	r = [a,b,c,d]
	return raise
	
	
# Shuffle and print the IP list.  Used with rando.
def showRandomized(ipList):
	random.shuffle(ipList)
	for ip in ipList:
		print ip
		
		
# --------------------------END FUNCTIONS----------------------------



# Check cmd line args
if len(sys.argv) < 2 or len(sys.argv) > 3:
	usage()
if len(sys.argv) == 3:
	if "-r" not in sys.argv[1]:
		usage()
	else:
		rando = 1
		arg = 2
		
		
		
# Check for network notation

# CIDR notation.  Preferred.  Takes into account network and broadcast addresses.
if "/" in sys.argv[arg]:
	ip,cidr = sys.argv[arg].split("/")
	a,b,c,d = ip.split(".")
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	cidr = int(cidr)
	
	ipRange = int(math.pow(2,32-cidr))
	
	# note the lack of print here, to skip the network address.
	for i in range(ipRange-2):
		ip = incrementIP(a,b,c,d)
		a,b,c,d = ip
		
		if rando == 1:
			ipList.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))
		else:
			showIP(a,b,c,d)
			
	if rando == 1:
		showRandomized(ipList)
		
	quit()
	
	
	
# Range of IP addresses.
elif "-" in sys.argv[arg]:
	rng1, rng2 = sys.argv[arg].split("-")
	octets1 = rng1.split(".")
	octets2 = rng2.split(".")
	
	if len(octets1) == 4 and len(octets2) == 1:
		# 192.168.5.21-65
		a = int(octets1[0])
		b = int(octets1[1])
		c = int(octets1[2])
		d = int(octets1[3])
		tA = a
		tB = b
		tC = c
		tD = int(octets2[0])
			
			
	elif len(octets1) == 3 and len(octets2) == 2:
		# 192.168.5-6.255
		a = int(octets1[0])
		b = int(octets1[1])
		c = int(octets1[2])
		d = 0
		tA = a
		tB = b
		tC = int(octets2[0])
		tD = int(octets2[1])
		
			
	elif len(octets1) == 2 and len(octets2) == 3:
		# 192.168-25.255.54
		a = int(octets1[0])
		b = int(octets1[1])
		c = 0
		d = 0
		tA = a
		tB = int(octets2[0])
		tC = int(octets2[1])
		tD = int(octets2[2])
		
			
	elif len(octets1) == 1 and len(octets2) == 4:
		# 192-193.255.253.7
		a = int(octets1[0])
		b = 0
		c = 0
		d = 0
		tA = int(octets2[0])
		tB = int(octets2[1])
		tC = int(octets2[2])
		tD = int(octets2[3])
		
			
	else:
		print "Invalid IP range entered."
		usage()
		
		
	while a != tA or b != tB or c != tC or d != tD:
		if rando:
			ipList.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))
		else:
			showIP(a,b,c,d)
		a,b,c,d = incrementIP(a,b,c,d)
	if rando:
		ipList.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))
	else:
		showIP(a,b,c,d)
		
	if rando:
		showRandomized(ipList)
		
	quit()
	
	
	
# Wildcarded octet
elif "*" in sys.argv[arg]:
	a = 0
	b = 0
	c = 0
	d = 0
	octets = sys.argv[arg].split(".")
	
	if len(octets) == 4:
		if "*" in octets[3]:
			a = int(octets[0])
			b = int(octets[1])
			c = int(octets[2])
			ipRange = int(math.pow(2,8)) - 1
			
	elif len(octets) == 3:
		if "*" in octets[2]:
			a = int(octets[0])
			b = int(octets[1])
			ipRange = int(math.pow(2,16)) - 1
			
	elif len(octets) == 2:
		if "*" in octets[1]:
			a = int(octets[0])
			ipRange = int(math.pow(2,24)) - 1
			
	else:
		print "Invalid IP range entered."
		usage()
		
	if rando:
		ipList.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))
	else:
		showIP(a,b,c,d)
		
	for i in range(ipRange):
		ip = incrementIP(a,b,c,d)
		a,b,c,d = ip
		
		if rando:
			ipList.append(str(a) + "." + str(b) + "." + str(c) + "." + str(d))
		else:
			showIP(a,b,c,d)
			
	if rando:
		showRandomized(ipList)
	quit()