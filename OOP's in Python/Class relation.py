


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

    def __str__(self):
        return f"{self.city}, {self.pincode}, {self.state}"


add = Address("Pune", "411035", "Maharashtra")
prem = Customer("Prem", "21", add)
print(prem)
