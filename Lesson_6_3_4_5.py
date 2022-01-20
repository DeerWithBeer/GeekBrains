import os
import pickle
import sys  # подключение модуля для командой строки

os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
from Support import makefile  # вспомогательный модуль для проверки. Создаёт файл по заданию

# вспомогательная функция для генерация файла по щаданному пути с заданным количеством пользователей, их хобби
makefile(10, 8)

dic_1 = {}  # болванка словаря для задания 3
dic_2 = {}  # болванка словаря для задания 4
# список аргументов с значениями по умолчанию
arguments = [
    __file__,  # имя скрипта
    'users.csv',  # путь к пользователям
    'hobby.csv',  # путь к хобби
    'result.pickle'  # путь к файлу результата
]
# перевод аргументов командной строки в список аргументов. Если аргумента нет, то остаётся значение по умолчанию
for i, val in enumerate(sys.argv, start=0):
    if i==len(arguments):break # если входных аргументов оказлось больше, выход из цикла
    arguments[i] = val
with open(arguments[1]) as user_file, open(arguments[2]) as hobby_file:
    for user in user_file:
        fio = user[:-1]  # получение ФИО с запятыми разделителями
        hobby = hobby_file.readline()[:-1]  # получение хобби с запятыми
        dic_1[fio.replace(',', ' ')] = hobby if len(hobby) != 0 else None
        # преобразование фамилии в кортеж. Кортеж, потому что ФИО не изменится и его можно использовать в качестве ключа
        fio = tuple(fio.split(','))
        # преобразование хобби в множество. Множество, потому что может быть так, что хобби могут случайно повторяться
        # а оно нам не надо
        hobby = set(hobby.split(',')) if len(hobby) != 0 else None
        dic_2[fio] = hobby
    if len(hobby_file.readline()) != 0:  # проверка если файл с хобби не был прочитан до конца, то выход из программы
        user_file.close()
        hobby_file.close()
        quit(1)
with open(arguments[3], 'wb') as result_file:  # запись словаря в файл двоичного формата (так просто проще хранить)
    pickle.dump(dic_1, result_file)
print(dic_2)
