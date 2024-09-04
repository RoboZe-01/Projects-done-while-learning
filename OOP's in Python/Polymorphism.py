

class Phone :
    def __init__(self,brand , price) :
        
        print("Inside a Phone Construbctor ")

        self.brand = brand
        self.price = price

class Smartphone(Phone) :
    def __init__(self,brand,price,camera,os,ram) :
        super().__init__(brand,price)
        self.camera = camera
        self.os = os
        self.ram = ram
        print("Inside Smartphone constructor")


Smart1 = Smartphone("samsung","30000","50 Mp","Snapdragon","16 gb")
print(Smart1)
print(Smart1.price)

        