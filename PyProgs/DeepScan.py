import socket
import itertools
import concurrent.futures
import time

# Displaying a message before the script starts
print('Deep IP Scanner by STRMBRG & OpenAI')
time.sleep(0.8)

# Initialization of global variables to keep track of the number of scanned IP addresses and the total number of IP addresses.
scanned_count = 0
total_ips = 0

# Function declaration named "scan". It takes two arguments: "ip" (IP address) and "port" (port).
def scan(ip, port):
    global scanned_count
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f'Found IP: {ip} | Port: {port}')
            with open('workingips.txt', 'a') as f:
                f.write(f'{ip}:{port}\n')
        if port == ports_list[-1]:
            scanned_count += 1
            print(f'Progress: {scanned_count}/{total_ips} IPs scanned')

# Obtaining ports to scan from the user
ports_string = input('Enter ports to scan separated by commas (for example 80,443): ')
# Split the string with ports into a list and convert each element into a number
ports_list = [int(port.strip()) for port in ports_string.split(',') if port.strip().isdigit()]

# Read IPs to scan from file
with open('ipranges.txt', 'r') as f:
    ips_to_scan = []
    for line in f.readlines():
        start_ip, end_ip = line.strip().split('-')
        start_parts = list(map(int, start_ip.split('.')))
        end_parts   = list(map(int, end_ip.split('.')))
        ip_ranges   = [range(start_parts[i], end_parts[i]+1) for i in range(4)]
        for a, b, c, d in itertools.product(*ip_ranges):
            ips_to_scan.append(f'{a}.{b}.{c}.{d}')
    total_ips = len(ips_to_scan)  # Set the total number of IPs to be scanned

# Get the number of threads to use
num_threads = int(input('Enter the number of threads: '))

# Scan IPs and ports using multiple threads
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    for ip in ips_to_scan:
        for port in ports_list:
            executor.submit(scan, ip, port)

print('Scanning completed. Active IPs and their ports are recorded in workingips.txt')
