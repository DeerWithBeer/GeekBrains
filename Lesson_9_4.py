class Car:
    def __init__(self,color='Unknowed',name='Unknowed',speed=0,is_police=False):
        self.name=name
        self.color = color
        self.speed=speed
        self.is_police=is_police
    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self,direction='налево'):
        print(f'Машина {self.name} повернула {direction}')
    def show_speed(self):
        print(f'Скорость машины {self.name}:{self.speed}')
        return self.speed
class TownCar(Car):
    def show_speed(self):
        if super().show_speed()>60:
            print(f'Машина {self.name} превысила скорость')
class SportCar(Car):
    ...
class WorkCar(Car):
    def show_speed(self):
        if super().show_speed()>40:
            print(f'Машина {self.name} превысила скорость')
class PoliceCar(Car):
    def __init__(self,color='Unknowed',name='Unknowed',speed=0):
        super().__init__(color='Unknowed',name='Unknowed',speed=0,is_police=True)
car_1=TownCar('Красная','mazda',70)
car_1.show_speed()