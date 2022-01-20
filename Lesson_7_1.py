import os
def create_project(dirs, path='./'): # рекурсивная функция для прсомотра всего словаря папок.
    for dir in dirs:
        if not os.path.isdir(path + dir):  # если папки не существует, то создать её
            os.mkdir(path + dir)
        if dirs[dir]: # если зачение словаря не пустое, то вызвать функцию
            create_project(dirs[dir], path + dir + '/')
os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
dir_dict= {
    'my_project':{
                     'settings':None,
                     'mainapp':None,
                     'adminapp':None,
                     'authapp':None
                }
} # список директроий и их структура в виде словаря
create_project(dir_dict)