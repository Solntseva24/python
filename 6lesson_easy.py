# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, car_name):
        self.name = car_name

    def go(self):
        print('поехала')

    def stop(self):
        print('остановилась')

    def turn(self):
        print('повернула')
my_TownCar = TownCar('машинка')
my_TownCar.name
my_TownCar.go()
my_TownCar.stop()
my_TownCar.turn()
print(my_TownCar.name)

class SportCar(TownCar):

self.speed = my_sportCar('быстрая')

class WorkCar(SportCar):

self.color = my_workCar('красивого цвета')

class PoliceCar(WorkCar):

self.is_police = my_workCar('полицейская')




# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
super().__init__(car_name)