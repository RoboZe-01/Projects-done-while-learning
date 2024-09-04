

class Customer :
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender 

def greet(self):
    if self.gender == "male":

        print("Hello",self.name,"Sir") 
    else :
        print(f"Hello {self.name} Ma'am")

cust = Customer("Prem","Female") 
greet(cust)           
    