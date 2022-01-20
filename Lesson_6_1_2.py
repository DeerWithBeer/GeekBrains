import os

os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
result = []
count_of_request = {}  # болванка для словаря количеств запросов
with open('nginx_logs.txt') as file:
    for line in file:  # цикл чтения файла
        remote_addr = line[:line.find(' - - ')]  # нахождение ip
        request_type = line[line.find(' "') + 2:line.find('" ')].split()[0]  # нахождение типа запроса
        requested_resource = line[line.find(' "') + 2:line.find('" ')].split()[1]  # нахождение запрашиваемого
        result.append((remote_addr, request_type, requested_resource))  # присоеденение нового кортежа к результату
        if count_of_request.get(remote_addr):  # если такой IP есть, то увеличить счётчик
            count_of_request[remote_addr] += 1
        else:  # если IP нет, то создать ключ для записи
            count_of_request[remote_addr] = 1
spammer = ('Спаммер не найден', 0)  # болванка для кортежа про спаммера
for key in count_of_request:  # классический алгоритм поиска наибольшего значения полным перебором
    if count_of_request[key] > spammer[1]: spammer = (key, count_of_request[key])
print(*result, sep='\n')  # печать результата
print(f'Спаммер: {spammer[0]}, его количество запросов: {spammer[1]}')  # печать ip спаммера и количества его запросов
