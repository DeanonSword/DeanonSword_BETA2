def create_credentials_file():
    with open('credentials.txt', 'w') as file:
        file.write('user1,password1\n')
        file.write('user2,password2\n')
        # Здесь можно добавить другие логины и пароли

def check_credentials(username, password):
    with open('credentials.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                return True
        return False

# Проверяем, существует ли файл с логинами и паролями, и если нет - создаем его
try:
    open('credentials.txt', 'r')
except FileNotFoundError:
    create_credentials_file()

# Пример использования
while True:
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if check_credentials(username, password):
        print("Доступ разрешен")
        # Здесь можно добавить код для продолжения работы программы
        break
    else:
        print("Ошибка: неверный логин или пароль. Попробуйте снова.")

import time

print("Запускаем обратный отсчет...")
for i in range(5, 0, -1):
    
    time.sleep(1)

print("Пуск!")
# Здесь можно добавить код, который нужно выполнить после обратного отсчета

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  

clear_terminal()


print ('🇩‌🇴‌🇧‌🇷‌🇴‌ 🇵‌🇴‌🇿‌🇭‌🇦‌🇱‌🇴‌🇻‌🇦‌🇹‌') 
from banner import banner
from pystyle import *

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

print(Colorate.Horizontal(Colors.red_to_white,Center.XCenter(banner)))
select = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["BOLD"]} Выбрать >{COLOR_CODE["RED"]} ')
if select == '1':
    from deanon import get_number
    database_file = 'AkumaNumber.csv' 
    search_value = input(f'{COLOR_CODE["YELLOW"]}[@]номер телефона сюды>:')
    get_number(database_file, search_value)
elif select == '2':
    print('временно не доступно')
elif select == '3':
    from get_ip import get_ip
    get_ip()
elif select =='4':
    from ddos import dos
    dos()
elif select == '2':
    print('Временно не доступно')
elif select == '7':
    from deanon_username import deanon_username
elif select =='6':
    exit