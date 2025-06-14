import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_host(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((str(ip), port))
        print(f"[+] {ip}:{port} is open")
        s.close()
    except:
        pass

network = ipaddress.ip_network("192.168.100.84/24", strict=False)
ports = [22, 80, 443]

with ThreadPoolExecutor(max_workers=100) as executor:
    for ip in network.hosts():
        for port in ports:
            executor.submit(scan_host, ip, port)

