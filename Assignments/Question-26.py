# What is Instantiation in terms of OOP terminology?

class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

brand = input("Enter Car's brand name :")
model = input("Enter Your model Name like to You :")
my_car = Car(brand,model)


my_car.display_info()  
