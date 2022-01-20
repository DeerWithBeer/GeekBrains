import os
import sys  # подключение модуля для командой строки

os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
arguments = []  # болванка для аргументов
# перевод аргументов командной строки в список аргументов. Если аргумента нет, то он не добавляется.
# Если формат ключевы харгументво не переводим то вхыодит ошибка
for i, val in enumerate(sys.argv, start=0):
    arguments.append(val)
    if i in (1, 2):
        if arguments[i].isdigit():
            arguments[i] = (int)(arguments[i])
        else:
            print(f'Неверно задан аргумент №{i}')
            exit(1)
with open('bakery.csv', 'r',encoding='utf-8') as file:
    if len(arguments) == 1:
        for line in file:
            print(line.strip())  # печать значения
    if len(arguments) == 2:
        for i,line in enumerate(file, start=1):
            if i >= arguments[1]:
                print(line.strip()) # печать значения начиная с индекса
    if len(arguments) == 3:
        for i,line in enumerate(file, start=1):
            if i >= arguments[1] and i<=arguments[2]:
                print(line.strip()) # печать значения начиная с индекса