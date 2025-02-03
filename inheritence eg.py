# Parent Class: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Child Class: Car
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

# Child Class: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, helmet_required):
        super().__init__(brand, model)
        self.helmet_required = helmet_required

    def display_info(self):
        super().display_info()
        print(f"Helmet Required: {'Yes' if self.helmet_required else 'No'}")

# Example Usage
car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "MT-15", True)

print("\nCar Details:")
car.display_info()

print("\nBike Details:")
bike.display_info()







class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"{self.account_holder}'s Balance: ₹{self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        print(f"Interest added! New Balance: ₹{self.balance:.2f}")
savings = SavingsAccount("Akarsh Gowda", 5000, 5)
savings.display_balance()
savings.add_interest()
