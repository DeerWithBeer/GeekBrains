import os

os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
folder = './'
result_dic = {}
fuul_dir = os.walk(folder)
for dirpath, dirnames, filenames in fuul_dir:
    # перебрать каталоги
    for file in filenames:
        path = os.path.join(dirpath, file)
        size = os.stat(path).st_size
        key = 10
        while size > 0:
            size = size // 10
            key *= 10
        if result_dic.get(key):
            result_dic[key][0] += 1
            result_dic[key][1].add(os.path.splitext(path)[1])
        else:
            result_dic[key] = [1, set(os.path.splitext(path)[1])]
for key in result_dic:
    # преобразуем множетсва в список, а значение словаря в кортеж
    result_dic[key] = (result_dic[key][0], list(result_dic[key][1]))
print(result_dic)
