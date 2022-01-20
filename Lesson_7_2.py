import os
os.chdir(os.path.dirname(__file__))  # Выбор текущей директории (на всякий случай)
path_list=['.'] # список текущего пути
p_level=-1 # перменаня для хранения предыдущего уровня иерархии
# структуа файла идёт по принципу табуляции. Папки обозначаются :.
# был выбран алгоритм чтения файла (вместо промежуточного занесения в список) т.к.:
# это быстрее по скорости
with open('config.yaml','r') as config:
        for line in config:
            c_level=line.count('    ') # текущий уровень иерархии
            line=line.replace(('    '), '').replace('\n', '')  # очистка строки от лишнего
            end=line[-1] # получение окончания файла
            for i in range(p_level-c_level): #у меньшение уровня иерархии и удаление из списка
                path_list.pop()
            p_level=c_level
            line=line.replace(':','')
            path_list.append(line)
            path='/'.join(path_list)
            if end== ':':
            # Если папка, то создать    ё (если ещё нет) и увеличить предыдущий уровень на 1
                if not os.path.isdir(path): os.mkdir(path)
                p_level+=1
            else:
                file=open(path, 'w')
                file.close()
                path_list.pop()
