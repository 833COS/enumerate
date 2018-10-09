# enumerate
A replacement for the venerable expand_net script

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
