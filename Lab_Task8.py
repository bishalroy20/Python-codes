# Procedural style
def calculate_area(length, width):
    return length * width


# oop style
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print(r.calculate_area())



# oop Encapsulation

class Person:
    def __init__(self, name):
        self.__name = name   # Private variable
    
    def get_name(self):
        return self.__name




# oop inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()



#oop polymorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.speak()



# Iterators
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)



# Generators
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)


# Clousers
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))   # 8
