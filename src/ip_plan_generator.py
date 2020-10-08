import ipaddress
import argparse

# Things to ask
# Number of VPRNs
# Architecture Mode: LB-Mode, LB-Less
# Redundancy Scheme: NK, One-to-One
# Number of Active MG-VMs
# VLAN Mode: VST or VGT


# Networks to be calculated

# Cloud Networks
# OAM OOB
# DB OOB
# DB External 

# Application Networks
# For NK with VGT

# Number of VPRNs times number of LB Ports, 
# gives the total number of P2P connections for BGP

# Number of VPRNs gives the total number of BGP Loopbacks
# If BBIP loopbacks are needed, add 2 loopbacks per VPRN


class NetworkPlanner:
    pass

    def create_ciq(self):
        pass

class LBMode(NetworkPlanner):
    pass

class LBLess(NetworkPlanner):
    pass

class NKRedundancy:
    pass

class OnetoOneRedundancy:
    pass

