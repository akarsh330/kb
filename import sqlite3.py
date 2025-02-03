import sqlite3

# Database connection
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Creating tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Person (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    room_number INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS PrimeCustomer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    room_number INTEGER,
                    discount INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS StaffMember (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    role TEXT)''')

conn.commit()

# Parent Class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save_to_db(self):
        cursor.execute("INSERT INTO Person (name, age) VALUES (?, ?)", (self.name, self.age))
        conn.commit()

# Child Class: Customer
class Customer(Person):
    def __init__(self, name, age, room_number):
        self.name = name
        self.age = age
        self.room_number = room_number

    def save_to_db(self):
        cursor.execute("INSERT INTO Customer (name, age, room_number) VALUES (?, ?, ?)", 
                       (self.name, self.age, self.room_number))
        conn.commit()

# Child Class: PrimeCustomer (inherits from Customer)
class PrimeCustomer(Customer):
    def __init__(self, name, age, room_number, discount):
        self.name = name
        self.age = age
        self.room_number = room_number
        self.discount = discount

    def save_to_db(self):
        cursor.execute("INSERT INTO PrimeCustomer (name, age, room_number, discount) VALUES (?, ?, ?, ?)", 
                       (self.name, self.age, self.room_number, self.discount))
        conn.commit()

# Child Class: StaffMember
class StaffMember(Person):
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def save_to_db(self):
        cursor.execute("INSERT INTO StaffMember (name, age, role) VALUES (?, ?, ?)", 
                       (self.name, self.age, self.role))
        conn.commit()

# Example Usage
cust = Customer("Akarsh", 28, 101)
cust.save_to_db()

prime_cust = PrimeCustomer("Rahul", 30, 202, 10)
prime_cust.save_to_db()

staff = StaffMember("Suresh", 35, "Manager")
staff.save_to_db()

# Fetch and display Customer Data
cursor.execute("SELECT * FROM Customer")
print("\nCustomers in Database:")
for row in cursor.fetchall():
    print(row)

# Fetch and display Prime Customer Data
cursor.execute("SELECT * FROM PrimeCustomer")
print("\nPrime Customers in Database:")
for row in cursor.fetchall():
    print(row)

# Fetch and display Staff Data
cursor.execute("SELECT * FROM StaffMember")
print("\nStaff Members in Database:")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
