import socket
import threading
import time

# Выводим сообщение перед началом работы скрипта
print('Port Scanner by STRMBRG & OpenAI')
time.sleep(1)

ip_address = input("Введите IP-адрес для сканирования портов: ")
min_port = int(input("Введите начальный порт для сканирования: "))
max_port = int(input("Введите конечный порт для сканирования: "))
delay = float(input("Введите задержку (в секундах) между проверками портов: "))

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1) # Установка таймаута в 0.1 секунды
    result = s.connect_ex((ip_address, port))
    if result == 0:
        print(f"Порт {port} открыт")
        open_ports.append(port)
    else:
        print(f"Порт {port} закрыт")
    s.close()

threads = []

for port in range(min_port, max_port+1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()
    time.sleep(delay)

for t in threads:
    t.join()

print("Открытые порты:")
print(open_ports)