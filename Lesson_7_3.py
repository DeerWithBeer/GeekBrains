import os
import shutil
os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
fuul_dir=os.walk('./my_project')
dir_templates='./my_project/templates'
if not os.path.isdir(dir_templates):  # если папки не существует, то создать её
    os.mkdir(dir_templates)
for dirpath, dirnames, filenames in fuul_dir:
    # перебрать каталоги
    for dirname in dirnames:
        if dirname=='templates':
            print(os.path.join(dirpath,dirname))
            # Функция копирования всего дерева и игнорирование, если директория уже существует
            shutil.copytree(os.path.join(dirpath,dirname), dir_templates, dirs_exist_ok=True)




