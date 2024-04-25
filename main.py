import os
import sys
import openPorts

if len(sys.argv) < 2:
    print("Usage: python main.py <IP>")
    sys.exit(1)

target_host = sys.argv[1]
open_ports = openPorts.scan_ports(target_host)
os.system(f"./flag1.sh {target_host} {open_ports[1]}")
