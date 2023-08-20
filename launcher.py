import os
import time

# Создаем список доступных программ
programs = {
    "1": "DeepScan.py",
    "2": "PortScan.py"
}

# Выводим сообщение перед началом работы скрипта
print('Launcher by STRMBRG & OpenAI')
time.sleep(1)

# Выводим список программ на экран
print("Доступные программы:")

for key, value in programs.items():
    print(f"{key}. {value}")

# Получаем от пользователя номер выбранной программы
program_number = input("Введите номер программы: ")

# Запускаем выбранную пользователем программу, если она есть в списке доступных
if program_number in programs:
    program_name = programs[program_number]
    
    # Проверяем существование файла с указанным именем и запускаем его при наличии
    if os.path.isfile(f"PyProgs/{program_name}"):
        os.system(f"python PyProgs/{program_name}")
        
        print(f"Программа {program_name} завершена")
    
    else:
        print(f"Ошибка: программа {program_name} не найдена!")
else:
    print("Ошибка: неверный номер программы!")