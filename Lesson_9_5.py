class Stationery:
    def __init__(self,name=''):
        self.name=name
    def draw(self):
        print(f'Запуск отрисовки {self.name}')
class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.name} рисует')
class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.name} рисует')
class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.name} рисует')
list_of_object=[]
list_of_object.append(Pen('Чёрная'))
list_of_object.append(Pencil('Красный'))
list_of_object.append(Handle('Красный'))
for stationery in list_of_object:
    stationery.draw()