import os
import sys  # подключение модуля для командой строки
os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
if len(sys.argv)<2:
    print('Не указана сумма продажи')
    exit(1)
arguments = [
    __file__,  # имя скрипта
    0,  # путь к пользователям
    0,  # путь к хобби
]
# перевод аргументов командной строки в список аргументов. Если аргумента нет, то остаётся значение по умолчанию
for i, val in enumerate(sys.argv, start=0):
    arguments[i] = val
with open('bakery.csv','a',encoding='utf-8') as file:
    file.write(sys.argv[1]+'\n')