# importing the module 
import tweepy
import random

messages = [
    "The IEEE protocol for STP is 802.1D.",
    "The root port is the port closest to the root switch. Root ports are always in forwarding state.",
    "The 8-byte Bridge ID is made up of:\nPriority field = 2 bytes\nSystem ID based on MAC address = 6 bytes",
    "A switchports default port priority is 128. The lower the priority the better.",
    "The normal VLAN range is 1-1005.",
    "The extended range of VLANs are 1006-4094.",
    "The native VLAN is not tagged.",
    "VLANs 1, and 1002-1005 cannot be deleted",
    "The following commands can be used to disable VTP:\nvtp mode transparent\nvtp mode off",
    "Switches use Dynamic Trunking Protocol (DTP) to negotiate trunking.",
    "Access, Trunk, Dynamic Desireable and Dynamic Auto are the administrative modes of a switchport",
    "The default administrative mode of a switchport is Dynamic Auto.",
    "The command to disable DTP is:\nswitchport nonegotiate",
    "TCP uses a 3-way handshake to establish a reliable connection. The 3-way handshake consists of a SYN, SYN-ACK, and ACK.",
    "The Layer 2 broadcast destination address is FFFF.FFFF.FFFF.",
    "The Layer 3 broadcast destination address is 255.255.255.255.",
    "The Physical layer of the OSI Model defines the physical characteristics of the transmission medium. Protocols & Specifications include RJ-45 and Ethernet. Devices include a LAN hub, LAN repeater, and cables.",
    "The Data Link layer of the OSI Model defines the protocols for deliverin data over a particular single type of physical network.\nProtocols: HDLC, Ethernet.\nDevices: LAN Switch, WAP, Cable & DSL Modem.",
    "The Network Layer of the OSI Model defines logical addressing, routing, and the routing protocols to learn routes.\nProtocols: IP.\nDevices: Router.",
    "The Transport Layer of the OSI Model focuses on data delivery between the two endpoint hosts.\nProtocols: TCP, UDP.\nDevices: Hosts, Firewalls.",
    "The Session Layer of the OSI Model is responsible for setting up, managing, and tearing down sessions between Presentation layer entities. Also provides dialogue control between devices. Protocols: SCP, PAP, RTCP.",
    "The command 'copy startup-config running-config' will enable a router to copy the configuration files from NVRAM to RAM.",
    "The router with the highest priority will be the designated router (DR) on an OSPF network segment.",
    "The command 'show ip protocols' can be used to verify the routes which are summarized for an interface.",
    "The default interval used by Cisco Discovery Protocol (CDP) to send updates is 60 seconds.",
    "The command 'no cdp advertise-v2' is used to disable the Cisco Discovery Protocol Version 2 (CDPv2) advertisements.",
    "A rollover crossover cable is used to connect the console port on the switch to a terminal.",
    "The command 'show port-security <int-id>' displays all port security settings for a specific interface.",
    "Jitter is one type of delay variation that is common with voice traffic.",
    "A switch uses Spanning Tree Protocol (STP) in order to create a loop-free environment.",
    "There is no difference between information security requirements for virtual servers and physical servers.",
    "On-Demand Routing allows Cisco Discovery Protocol (CDP) to include information in its periodic update messages to neighboring devices.",
    "EIGRP and IGRP both perform equal and unequal load balancing by default.",
    "The device name and domain name must be provided to generate the SSH encryption key.",
    "The FTP protocol operates at OSI layer 7 (Application Layer).",
    "The Southbound API is used to communicate with data place devices such as routers, switches and firewalls.",
    "Asymmetric Routing causes a ping packet to take a different path in the return than it did on its way to the destination.",
    "192.168.0.0 to 192.168.255.255 is the range of Private address for Class C IP addresses.",
    "The fragment-free switching process only waits to receive the first 64 bytes of the frame before forwarding it to the destination port.",
    "switch(config)#ip routing\nThis command enables routing on a multilayer switch.",
    "QUICK QUIZ:\nWhat would the broadcast address be if the IP address given is 192.168.0.1 and the subnet mask is 255.255.255.192?",
    "An IPv6 address is 128 bits in length.",
    "A LAN Bridge provides software-based switching of LAN traffic.",
    "A switch will forward broadcast traffic to all ports except the port on which it was received.",
    "The three types of switching processes are:\nStore and forward, cut-through, and fragment-free.",
    "QUICK QUIZ:\nHow many collision domains does a 24-port switch create?",
    "A switch will forward multicast frame to all ports except the port on which it was received.",
    "Three approaches for troubleshooting network problems using the OSI layered model are:\nTop Down, Bottom Up, and Divide and Conquer.",
    "QUICK QUIZ:\nWhat is the maximum number of subnets that will be created with IP address 192.168.1.1 and subnet mask of 255.255.255.240?",
    "The command 'show vtp domain' will display VLAN Trunking Protocol (VTP) domain information.",
    "Cisco Discovery Protocol (CDP) operates at Layer 2 but is capable of obtaining Layer 3 IP address information for directly connected neighboring devices.",
    "The command 'show vtp counters' lets you view VLAN Trunking Protocol (VTP) statistics information.",
    "Switches use VLANs for LAN segmentation.",
    "Entering command 'cdp run' in global configuration will enable Cisco Discovery Protocol (CDP) on a Cisco device.",
    "Entering command 'cdp timer' in global configuration will let you configure the frequency at which the Cisco IOS sends Cisco Discovery Protocol (CDP) updates.",
    "COMMAND: show spanning-tree vlan <vlan-id>\nThis is used to view information regarding the spanning tree for a particular VLAN.",
    "Multiple VLAN protocol IEEE 802.1Q is used to connect multiple switches and routers together.",
    "Cisco Discovery Protocol (CDP) operates at Layer 2 of the OSI Model.",
    "COMMAND: no cdp run\nThis is used to disable Cisco Discovery Protocol (CDP) on a Cisco router.",
    "VTP Client mode does not save VLAN information in NVRAM.",
    "Network congestion is one of the causes of jitter in the IP network.",
    "When you run the command 'show ip route', the S will imply that it is a static route.",
    "ip default-gateway <gateway address>\n\nThis is the global config command that will configure a default gateway on the router.",
    "show ip ospf neighbor\n\nThis command is used to verify the OSPF neighbor relationship.",
    "Virtual Router Redundancy Protocol (VRRP) provides backup for an assigned real IP address.",
    "The administrative distance (AD) for Open Shortest Path First (OSPF) is 110.",
    "show ip protocols\n\nThis command is used to view the current state of the active routing protocol process.",
    "Routing Information Protocol (RIP) uses hop-count metric for its path selection.",
    "The backbone area (area 0) must be configured on the area border routers (ABRs).",
    "When you run the command 'show ip route', the C will imply that there is a directly connected route.",
    "show ip ospf database\n\nThis command is used to view the OSPF database for a router.",
    "The router with the highest priority will become the designated router (DR) on an OSPF network segment.",
    "The OSPF default area 0 is commonly known as the Backbone area.",
    "EIGRP and IGRP are Cisco proprietary routing protocols.",
    "ip helper-address\n\nThis command is used to enable DHCP relay agent on a specific router interface.",
    "DHCPOFFER and DHCPACK messages are unicast messages.",
    "Device name and domain name must be provided to generate the SSH encryption key.",
    "TFTP uses port 69.",
    "The Edit NAT Configuration window on the SDM shows the configured dynamic NAT configuration.",
    "You can restrict remote access to SSH only via the VTY lines.",
    "TFTP operates on the Application Layer (Layer 7) of the OSI model.",
    "QUICK QUIZ: Which protocol does FTP use?\nTCP or UDP?",
    "A DHCP relay agent enables a host to acquire an IP address from a DHCP server located on a different subnet.",
    "The management information in SNMP is stored in the Management Information Base.",
    "FTP operates at the Application layer (Layer 7) of the OSI model.",
    "PAP is a PPP authentication method which transmits in clear text.",
    "show port-security [interface interface-id | address]\n\nThis command displays the status of port security on the specified interface of a switch.",
    "MAC filtering is used to allow or deny a connection based on the client's MAC address.",
    "WPA3 security protocol requires all connections to use Protected Management Frames (PMFs).",
    "shutdown, restrict, and protect\n\nThese are three configuration modes for the 'switchport port-security violation' command.",
    "CHAP uses a one-way hash function based on the MD5 hashing algorithm to hash the password.",
    "CHAP is a PPP authentication method that never sends the password across the network.",
    "Cisco Self-Defending Network strategy aims at making an organisation's business secure by identifying, preventing, and adapting to security threats.",
    "ESP should be selected to encrypt and transmit data between peer routers with high confidentiality.",
    "WPA3 Enterprise security protocol requires 192-bit AES keys.",
    "The asymmetric encryption algorithm is RSA.",
    "enable secret\n\nThis command is used to configure an encrypted enable secret password for privileged exec mode on a router.",
    "show port security\n\nThis command is used to view the configuration for port security.",
    "Rollback procedures should be included for every step in the implementation plan for redundant devices to provide for high availability in case of failure.",
    "All traffic will be blocked if you apply an ACL on an interface with no permit statements.",
    "The .json REST API suffix uses object orientation to categorise data into properties.",
    "Cisco DNA Center improves security by providing encrypting traffic analysis and multi-domain policy segmentation.",
    "The Southbound API communicated with data place devices such as routers, switches, and firewalls.",
    "Network underlay represents the physical network in an SDN environment.",
    "Caching in RSP API allows for the scaling of the application.",
    "The REST API uses a client/server architecture.",
    "The Northbound API communicates with higher level devices such as the network management station.",
    "In a Puppet stand-alone architecture, every node is installed with the application."
]
  
# personal details 
consumer_key ="0dAinYCW7sHH0148dXnB3Tvax"
consumer_secret ="Bi4C5SYJ9mCi6xfjwl7WPJoaBRW87UJ7KBX2rnp4Cs2w9HBHhc"
access_token ="1321780841039757317-I3LhdWw8Ctj3ZDY9nu6T9lvHc2WgMG"
access_token_secret ="xpwtjHzDkrvXGfR6qT2aeBm5DDEieXetNgCfS9JEGrk8x"
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status =random.choice(messages) + "\n#Cisco #CCNA #CCNATips")


#AAAAAAAAAAAAAAAAAAAAALn4JAEAAAAAo%2BkCIBFljpgaYDAJhWJQQdDFTPQ%3DNYJ0wWBvKMV5GfWcrnDyn9Mif3ohCXFjKV23r3k57A2zRYVsPI
