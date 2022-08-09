
from sys import argv
from abc import ABC, abstractmethod
from PIL import Image
cars = {
    "lada": {
        "name":"Lada",
        "body":"Квадратный черный кузов",
        "wheel":"Квадратные черные колеса",
        "glass":"Отсутствие стекл",
        "logo":"LADA",
        "image":"cars_image/lada.png",
    },
    "audi": {
        "name":"Audi",
        "body":"Округлый синий кузов",
        "wheel":"Круглые колеса",
        "glass":"Синие стекла",
        "logo":"AUDI",
        "image":"cars_image/audi.png",
    },
    "volkswagen": {
        "name":"Volkswagen",
        "body":"Округлый синий кузов",
        "wheel":"Круглые колеса",
        "glass":"Светлые стекла",
        "logo":"VOLKSWAGEN",
        "image":"cars_image/volkswagens.png",
    },
    "ferrari": {
        "name":"Ferrari",
        "body":"Красный кузов",
        "wheel":"Черные колеса",
        "glass":"Зеленое стекло",
        "logo":"FERRARI",
        "image":"cars_image/ferrari.png",
    },
}

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




class CarBuilder(Builder):

    def __init__(self, car_data):
        self.car = Car(car_data["name"])
        self.data =car_data

    def build_body(self) -> None:
        self.car.body = self.data.get("body")
 
    def add_glass(self): 
        self.car.glass = self.data.get("glass")

    def add_wheel(self) -> None:
        self.car.wheel = self.data.get("wheel")

    def add_logo(self) -> None:
        self.car.logo = self.data.get("logo")

    def add_image(self) -> None:
        self.car.image = Image.open(self.data.get("image"))

    def get_car(self) -> Car:
        self.build_body()
        self.add_glass()
        self.add_wheel()
        self.add_logo()
        self.add_image()
        self.car.image.show()
        return self.car




def get_car(name):
    cars_data = cars.get(name)
    if cars_data:
        builder = CarBuilder(cars_data)
        car=builder.get_car()   
        car.get_car_description()
    else: 
        print("Вы ввели некорректные данные, попробуйте ещё раз.")
   

if __name__=="__main__":
    if len(argv) == 1: 
        print("Выберите машину для создания и напишите его название:")
        for i in cars.keys():
            print(f"Название:{i}")
        name = input("Введите название:").lower()
        get_car(name)
    elif len(argv) == 2:
        name = argv[1].lower()
        cars_data = cars.get(name)
        get_car(name)