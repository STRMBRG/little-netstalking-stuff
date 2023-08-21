import socket
import threading
import time

# Displaying a message before the script starts
print('Port Scanner by STRMBRG & OpenAI')
time.sleep(0.8)

ip_address = input("Enter the IP address for port scanning: ")
min_port = int(input("Enter start port to scan: "))
max_port = int(input("Enter the destination port for scanning: "))
delay = float(input("Enter the delay (in seconds) between port checks: "))

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1) # Setting the timeout to 0.1 seconds
    result = s.connect_ex((ip_address, port))
    if result == 0:
        print(f"Port {port} open")
        open_ports.append(port)
    else:
        print(f"Port {port} closed")
    s.close()

threads = []

for port in range(min_port, max_port+1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()
    time.sleep(delay)

for t in threads:
    t.join()

print("Open ports:")
print(open_ports)
