import os
import sys
import openPorts

if len(sys.argv) < 2:
    print("Usage: python main.py <IP>")
    sys.exit(1)

target_host = sys.argv[1]
open_ports = openPorts.scan_ports(target_host)
if (len(open_ports) == 0):
    print("No open ports available")
    sys.exit(1)

print(f"All open ports: {open_ports}")
os.system(f"./flag1.sh {target_host} {open_ports[1]}")
os.system(f"./flag2.sh {target_host} {open_ports[-1]}")
os.system(f"./flag3.sh {target_host} {open_ports[-1]}")
os.system(f"./flag4.sh {target_host} {open_ports[-1]}")