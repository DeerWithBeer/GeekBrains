income_dic={
    'Ведущий':(45000,5000),
    'Первая категория': (35000,5000),
    'Вторая категория': (25000, 2500),
    'Третья категория': (15000, 1000),
    'Прочий персонал':(10000,500)
}
class Worker:
    def __init__(self,name,surname,position,income='Прочий персонал'):
        self.name=name
        self.surname=surname
        self.position=position
        self._income=income_dic[income]
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income[0]+self._income[1]
workers= []
workers.append(Position('Василий','Приходько','Рабочий','Вторая категория'))
workers.append(Position('Дмитрий','Забегайло','Консультант','Первая категория'))
workers.append(Position('Мария','Ивановна','Консультант','Вторая категория'))
workers.append(Position('Иван','Иванов','Рабочий'))
for worker in workers:
    print(f'{worker.get_full_name()}:{worker.get_total_income()}')
