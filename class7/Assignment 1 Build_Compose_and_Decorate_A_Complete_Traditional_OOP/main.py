
### 1. Using self
# Assignment: Create a class `Student` with attributes `name` and `marks`. Use `self` to initialize via constructor. Add a `display()` method.


from typing import List

class Student:
    def __init__(self, name: str, marks: List[float]):
        self.name = name
        self.marks = marks

    def display(self) -> None:
        print(f"Student: {self.name}, Marks: {self.marks}")

# Example usage
student = Student("Alice", [85.5, 90.0, 92.5])
student.display()





### 2. Using cls
# Assignment: Create a class `Counter` to track object count using a class variable and class method with `cls`.


class Counter:
    _count: int = 0

    def __init__(self):
        Counter._count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls._count

# Example usage
c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # Output: 2


### 3. Public Variables and Methods
# Assignment: Create a class `Car` with public variable `brand` and method `start()`.


class Car:
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> None:
        print(f"{self.brand} engine started!")

# Example usage
car = Car("Toyota")
print(car.brand)  # Output: Toyota
car.start()      # Output: Toyota engine started!

### 4. Class Variables and Class Methods
# Assignment: Create a class `Bank` with class variable `bank_name` and class method `change_bank_name()`.


class Bank:
    bank_name: str = "Global Bank"

    def __init__(self, account_holder: str):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name: str) -> None:
        cls.bank_name = name

# Example usage
b1 = Bank("Alice")
b2 = Bank("Bob")
print(b1.bank_name)  # Output: Global Bank
Bank.change_bank_name("Universal Bank")
print(b2.bank_name)  # Output: Universal Bank


### 5. Static Variables and Static Methods
# Assignment: Create a class `MathUtils` with static method `add()`.

class MathUtils:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

# Example usage
result = MathUtils.add(5.5, 3.2)
print(result)  # Output: 8.7

### 6. Constructors and Destructors
# Assignment: Create a class `Logger` with constructor and destructor messages.

class Logger:
    def __init__(self, name: str):
        self.name = name
        print(f"Logger {self.name} created")

    def __del__(self):
        print(f"Logger {self.name} destroyed")

# Example usage
log = Logger("SystemLog")
del log


### 7. Access Modifiers: Public, Private, and Protected
# Assignment: Create a class `Employee` with public, protected, and private variables.

class Employee:
    def __init__(self, name: str, salary: float, ssn: str):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

# Example usage
emp = Employee("Alice", 50000.0, "123-45-6789")
print(emp.name)       # Output: Alice
print(emp._salary)    # Output: 50000.0
try:
    print(emp.__ssn)  # Raises AttributeError
except AttributeError:
    print("Cannot access private variable __ssn")







### 8. The super() Function
# Assignment: Create a class `Person` and inherit `Teacher` using `super()`.


class Person:
    def __init__(self, name: str):
        self.name = name

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

# Example usage
teacher = Teacher("Alice", "Math")
print(f"{teacher.name} teaches {teacher.subject}")  # Output: Alice teaches Math




### 9. Abstract Classes and Methods
# Assignment: Create an abstract class `Shape` with abstract method `area()` and implement in `Rectangle`.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
# Example usage
rect = Rectangle(5.0, 3.0)
print(rect.area())  # Output: 15.0




### 10. Instance Methods
# Assignment: Create a class `Dog` with instance variables and method `bark()`.

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self) -> None:
        print(f"{self.name} says Woof!")

# Example usage
dog = Dog("Buddy", "Golden Retriever")
dog.bark()  # Output: Buddy says Woof!



### 11. Class Methods
# Assignment: Create a class `Book` with class variable `total_books` and class method `increment_book_count()`.


class Book:
    total_books: int = 0

    def __init__(self, title: str):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls) -> None:
        cls.total_books += 1


### 12. Static Methods
# Assignment: Create a class `TemperatureConverter` with static method `celsius_to_fahrenheit()`.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9/5) + 32

# Example usage
temp = TemperatureConverter.celsius_to_fahrenheit(25.0)
print(temp)  # Output: 77.0




### 13. Composition
# Assignment: Create classes `Engine` and `Car` with composition.




class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> None:
        print(f"Engine with {self.horsepower} HP started")

class Cars:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

    def start_car(self) -> None:
        print(f"{self.brand} car starting...")
        self.engine.start()


### 14. Aggregation
# Assignment: Create classes `Department` and `Employee` with aggregation.


class Employe:
    def __init__(self, name: str):
        self.name = name

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def list_employees(self) -> None:
        print(f"Employees in {self.name}: {[emp.name for emp in self.employees]}")


### 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment: Create classes `A`, `B`, `C`, and `D` to demonstrate MRO.


class A:
    def show(self) -> None:
        print("A's show")

class B(A):
    def show(self) -> None:
        print("B's show")

class C(A):
    def show(self) -> None:
        print("C's show")

class D(B, C):
    pass

# Example usage
d = D()
d.show()  # Output: B's show
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)



### 16. Function Decorators
# Assignment: Create a decorator `log_function_call` for a function `say_hello()`.


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello() -> None:
    print("Hello!")


### 17. Class Decorators
# Assignment: Create a class decorator `add_greeting` to add a `greet()` method.



def add_greeting(cls):
    def greet(self) -> str:
        return "Hello from Decorator!"
    setattr(cls, "greet", greet)
    return cls

@add_greeting
class Persons:
    def __init__(self, name: str):
        self.name = name

### 18. Property Decorators: @property, @setter, and @deleter
# Assignment: Create a class `Product` with property decorators for `_price`.


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self) -> None:
        del self._price


### 19. callable() and __call__()
# Assignment: Create a class `Multiplier` with `__call__()` and test with `callable()`.

class Multiplier:
    def __init__(self, factor: float):
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor

# Example usage
mult = Multiplier(2.0)
print(callable(mult))  # Output: True
print(mult(5.0))       # Output: 10.0


### 20. Creating a Custom Exception



class InvalidAgeError(Exception):
    pass

def check_age(age: int) -> None:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    print("Age is valid")

# Example usage
try:
    check_age(16)
except InvalidAgeError as e:
    print(e)  # Output: Age must be 18 or older



### 21. Make a Custom Class Iterable

class Countdown:
    def __init__(self, start: int):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Example usage
countdown = Countdown(5)
for num in countdown:
    print(num)  # Output: 5, 4, 3, 2, 1, 0

 
