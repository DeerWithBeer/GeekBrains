import time
class TrafficLight:
    def __init__(self, start_color='красный'):
        if start_color!='красный':
            raise ValueError('Неверно задан начальный цвет')
        self.__color=start_color;
    def running(self):
        print(f'Текущий цвет:{self.__color}')
        print(f'Ждите 7 секунд')
        time.sleep(7)
        self.__color='жёлтый'
        print(f'Текущий цвет:{self.__color}')
        print(f'Ждите 2 секунды')
        time.sleep(2)
        self.__color = 'зелёный'
        print(f'Текущий цвет:{self.__color}')
        print(f'Ждите 7 секунд')
        time.sleep(4)
        print(f'Работа светофора завершена')
traffic_light=TrafficLight()
traffic_light.running()
