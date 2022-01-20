import os

os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
folder = './'
if not os.path.isdir(folder):
    print('Папки не существует')
    exit(0)
result_dic = {}
fuul_dir = os.walk(folder)
for dirpath, dirnames, filenames in fuul_dir:
    # перебрать каталоги
    for file in filenames:
        size = os.stat(os.path.join(dirpath, file)).st_size
        key = 10
        while size > 0:
            size = size // 10
            key *= 10
        if result_dic.get(key):
            result_dic[key] += 1
        else:
            result_dic[key] = 1
print(result_dic)
