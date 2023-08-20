import socket
import itertools
import concurrent.futures
import time

# Выводим сообщение перед началом работы скрипта
print('Deep IP Scanner by STRMBRG & OpenAI')
time.sleep(1)

# Функция для проверки рабочих IP-адресов и записи их в файл
def scan(ip, ports):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        for port in ports:
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f'Working IP: {ip}:{port}')
                with open('workingips.txt', 'a') as f:
                    f.write(f'{ip}:{port}\n')

# Получаем порты для сканирования от пользователя
ports_string = input('Введите порты для сканирования через запятую (например 80,443): ')
# Разбиваем строку с портами на список и преобразуем каждый элемент в число
ports_list = [int(port.strip()) for port in ports_string.split(',')]

# Открываем файл с диапазонами IP-адресов и проходимся по каждому из них
with open('ipranges.txt', 'r') as f:
    # Создаем список всех IP-адресов из заданных диапазонов
    ips_to_scan = []
    for line in f.readlines():
        start_ip, end_ip = line.strip().split('-')
        start_parts = list(map(int, start_ip.split('.')))
        end_parts   = list(map(int, end_ip.split('.')))
        ip_ranges   = [range(start_parts[i], end_parts[i]+1) for i in range(4)]
        for a, b, c, d in itertools.product(*ip_ranges):
            ips_to_scan.append(f'{a}.{b}.{c}.{d}')

# Получаем количество потоков для сканирования от пользователя
num_threads = int(input('Введите количество потоков: '))

# Создаем пул потоков / корутин и выполняем параллельную проверку IP-адресов на рабочие порты
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Перебираем все IP-адреса в списке и отправляем задачу на проверку портов в пул потоков / корутин
    for ip in ips_to_scan:
        executor.submit(scan, ip, ports_list)

print('Сканирование завершено. Активные IP и их порты записаны в workingips.txt')