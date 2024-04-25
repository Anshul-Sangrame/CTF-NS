import nmap
import sys

def scan_ports(target_host):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_host, arguments='-p 1-65535 -T4')
    # nm.scan(hosts=target_host)
    print("Scanned all")
    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    open_ports.append(port)

    return open_ports

# # Check if command line arguments are provided
# if len(sys.argv) < 2:
#     print("Usage: python openPort.py <IP>")
#     sys.exit(1)

# target_host = sys.argv[1]
# open_ports = scan_ports(target_host)
# print("Open ports:", open_ports)
