"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"

    def show_speed(self):
        return f"Машина {self.name} движется со скоростью {self.speed} км/ч"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed} км/ч")

        if self.speed > 60:
            return f"Городская машина {self.name} едет слишком быстро."
        else:
            return f"Городская машина {self.name} едет с нормальной скоростью."


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):

        if self.name == "KIA Stinger":
            return f"Машина {self.name} спортивная."
        else:
            return f"Машина {self.name} не спортивная."


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Машина {self.name} движется со скоростью {self.speed} км/ч")

        if self.speed > 40:
            return f"Рабочая машина {self.name} едет слишком быстро."
        else:
            return f"Рабочая машина {self.name} едет с нормальной скоростью."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):

        if self.is_police:
            return f"Машина {self.name} полицейская."
        else:
            return f"Машина {self.name} не полицейская."


GOROD = TownCar(62, "Красная", "KIA Picanto", False)
SPORT = SportCar(100, "Синяя", "KIA Stinger", False)
WORK = WorkCar(32, "Черная", "KAMAZ", False)
POLICE = PoliceCar(120, "Белая", "ВАЗ 2109", True)

print(f"{SPORT.show_speed()}")
print(f"{GOROD.show_speed()}")
print(f"{POLICE.police()} И теперь она преследует автомобиль {GOROD.name}.")
print(f"Машина {SPORT.name} полицейская? {SPORT.is_police}")
print(f"Машина {POLICE.name} полицейская? {POLICE.is_police}")

print(GOROD.show_speed())
print(SPORT.sport())
print(WORK.show_speed())
print(POLICE.police())
