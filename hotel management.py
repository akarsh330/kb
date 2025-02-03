
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Customer(Person):
    def __init__(self, name, age, room_number):
        self.name = name
        self.age = age
        self.room_number = room_number

    def book_room(self):
        print(f"{self.name} booked Room {self.room_number}.")

class PrimeCustomer(Customer):
    def __init__(self, name, age, room_number, discount):
        self.name = name
        self.age = age
        self.room_number = room_number
        self.discount = discount

    def show_discount(self):
        print(f"{self.name} gets a {self.discount}% discount!")

class StaffMember(Person):
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def work(self):
        print(f"{self.name} is working as a {self.role}.")


cust = Customer("Akarsh", 28, 101)
prime_cust = PrimeCustomer("Rahul", 30, 202, 10)
staff = StaffMember("Suresh", 35, "Manager")

cust.display_info()
cust.book_room()

prime_cust.display_info()
prime_cust.book_room()
prime_cust.show_discount()

staff.display_info()
staff.work()
