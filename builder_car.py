
from sys import argv
from abc import ABC, abstractmethod
from PIL import Image

class Car:
    def __init__(self, name):
        self.name = name
        self.body = None
        self.wheel = None
        self.glass = None
        self.logo = None
        self.image = None

    def get_car_description(self):
        print(f"""
            Машина:{self.name}
            Кузов: {self.body}
            Колеса: {self.wheel}
            Стекла: {self.glass}
        """)

    def __str__(self) -> str:
        return self.name



class Builder(ABC):

    @abstractmethod
    def build_body(self) -> None: pass 

    @abstractmethod
    def add_wheel(self) -> None: pass 

    @abstractmethod
    def add_glass(self) -> None: pass 

    @abstractmethod
    def add_logo(self) -> None: pass 
    
    @abstractmethod
    def add_image(self) -> None: pass


    @abstractmethod
    def get_car(self) -> None: pass




class LadaBuilder(Builder):

    def __init__(self):
        self.car = Car("Lada")

    def build_body(self) -> None:
        self.car.body = "Квадратный черный кузов"
 
    def add_glass(self): 
        self.car.glass = "Отсутствуют"

    def add_wheel(self) -> None:
        self.car.wheel = "Квадратные колеса"

    def add_logo(self) -> None:
        self.car.logo = "Lada"

    def add_image(self) -> None:
        self.car.image = Image.open("cars_image/lada.png")

    def get_car(self) -> None:
        self.build_body()
        self.add_glass()
        self.add_wheel()
        self.add_logo()
        self.add_image()
        return self.car


class AudiBuilder(Builder):
    def __init__(self):
        self.car = Car("Audi")

    def build_body(self) -> None:
        self.car.body = "Округлый синий кузов"
 
    def add_glass(self): 
        self.car.glass = "Синие стекла"

    def add_wheel(self) -> None:
        self.car.wheel = "Круглые колеса"

    def add_logo(self) -> None:
        self.car.logo = "Audi"
    
    def add_image(self) -> None:
        self.car.image = Image.open("cars_image/audi.png")

    def get_car(self) -> None:
        self.build_body()
        self.add_glass()
        self.add_wheel()
        self.add_logo()
        self.add_image()
        return self.car


class VolkswagenBuilder(Builder):
    def __init__(self):
        self.car = Car("Volkswagen")

    def build_body(self) -> None:
        self.car.body = "Округлый синий кузов"
 
    def add_glass(self): 
        self.car.glass = "Светлые стекла"

    def add_wheel(self) -> None:
        self.car.wheel = "Круглые колеса"

    def add_logo(self) -> None:
        self.car.logo = "Volkswagen"
    
    def add_image(self) -> None:
        self.car.image = Image.open("cars_image/volkswagen.png")

    def get_car(self) -> None:
        self.build_body()
        self.add_glass()
        self.add_wheel()
        self.add_logo()
        self.add_image
        return self.car


class FerrariBuilder(Builder):
    def __init__(self):
        self.car = Car("Ferrari")

    def build_body(self) -> None:
        self.car.body = "Красный кузов"
 
    def add_glass(self): 
        self.car.glass = "Зеленое стекло"

    def add_wheel(self) -> None:
        self.car.wheel = "Черные колеса"

    def add_logo(self) -> None:
        self.car.logo = "Ferrari"

    def add_image(self) -> None:
        self.car.image = Image.open("cars_image/ferrari.png")

    def get_car(self) -> None:
        self.build_body()
        self.add_glass()
        self.add_wheel()
        self.add_logo()
        self.add_image()
        return self.car


cars_builders = {
    "lada": LadaBuilder,
    "audi": AudiBuilder,
    "volkswager": VolkswagenBuilder,
    "ferrari": FerrariBuilder,
}
def get_car(builder_class):
    builder = builder_class()
    car=builder.get_car()   
    car.get_car_description()
    car.image.show()

if __name__=="__main__":
    if len(argv) == 1: 
        print("Выберите машину для создания и напишите его название:")
        for i in cars_builders.keys():
            print(f"Название:{i}")
        name = input("Введите название:").lower()
        builder_class = cars_builders.get(name)
        if builder_class:
            get_car(builder_class)
        else: 
            print("Вы ввели некорректные данные, попробуйте ещё раз.")
    elif len(argv) == 2:
        car_name = argv[1].lower()
        builder_class = cars_builders.get(car_name)
        if builder_class: 
            get_car(builder_class)
        else: 
            print("Вы ввели некорректные данные, попробуйте ещё раз.")