# print helloworld using class
# class Helloworld:
#
#     def __init__(self, msg):
#         self.msg = msg
#     def display(self):
#         print(self.msg)
#
# msg1 = Helloworld("Hello World")
# msg1.display()
#
# print user input as output
# class prrint:
#
#     def __init__(self, num):
#         self.num = num
#     def display(self):
#         print(self.num)
#
# num = int(input())
# numprint = prrint(num)
# numprint.display()
#
# class Person(object):
#
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def Display(self):
#         print(self.name, self.id)
# emp = Person("Deebiga", 7)
# emp.Display()
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self, radius):
#         print(3.14 * self.radius * self.radius)
#
#     def calculate_perimeter(self, radius):
#         print(2 * 3.14 * self.radius)
#
#
# radius = 3
# circle = Circle(radius)
# circle.calculate_area(radius)
# circle.calculate_perimeter(radius)

# class Deebiga:
#     def func(self):
#         print("Deebiga")
#     def func1(self):
#         print("kathir")
# dee = Deebiga()
# # Deebiga.func(dee)
# dee.func1()

class Vehicle:
    def __init__(self, distance):
        self.distance = distance


class Car(Vehicle):
    def __init__(self, time):
        self.time = time

    def speed(self, distance, time):
        print(distance / time)


distance = int(input())
time = int(input())
obj1 = Vehicle(distance)
obj = Car(time)
obj.speed(distance, time)

