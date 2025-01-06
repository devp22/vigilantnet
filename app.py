from scapy.all import sniff, Ether

# Define a function to process captured packets
def packet_handler(packet):
    print(packet.summary())

# Sniff traffic on the default network interface (use 'iface' to specify a different interface)
# Call the packet_handler function for each captured packet
sniff(prn=packet_handler, count=10)
