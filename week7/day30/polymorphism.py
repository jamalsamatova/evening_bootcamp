# ПОЛИМОРФИЗМ - методы с одинаковым названием в разных классах работают по-разному

# class GrandPa:
#     def get_info(self):
#         print('Hello, is GrandPa class.')

# class Parent(GrandPa):
#     def get_info(self):
#         print('Hello, is Parent class.')

# class Child(Parent):
#     def get_info(self):
#         print('Hello, is Child class.')

# obj_grand = GrandPa()
# obj_parent = Parent()
# obj_child = Child()

# obj_child.get_info()
# obj_grand.get_info()
# obj_parent.get_info()


# class A:
#     def hello(self):
#         raise NotImplementedError()

# class B(A):
#     def hello(self):
#         print('Hello, world!')

# obj_b = B()
# obj_b.hello()


# class Worker:
#     pass

# class IT(Worker):
#     def __init__(self, salary):
#         self.salary = salary
    
#     def get_salary(self):
#         print(f'Salary is: {self.salary}')

# class HR(Worker):
#     def __init__(self, salary):
#         self.salary = salary
    
#     def get_salary(self):
#         print(f'Salary is: {self.salary}')

# class Driver(Worker):
#     def __init__(self, salary):
#         self.salary = salary
    
#     def get_salary(self):
#         print(f'Salary is: {self.salary}')

# it = IT(1500)
# it.get_salary()
# hr = HR(1000)
# hr.get_salary()
# driver = Driver(500)
# driver.get_salary()


# class King:
#     @staticmethod
#     def move():
#         print('Я хожу на 1 клетку в любую сторону.')
    
# class Queen:
#     @staticmethod
#     def move():
#         print('Я хожу как королева.')

# class Horse:
#     @staticmethod
#     def move():
#         print('Я хожу буквой Г')

# figure1 = King()
# figure2 = Queen()
# figure3 = Horse()

# figure1.move()
# figure2.move()
# figure3.move()



######################################################################
# abstract method
from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, pizza, cost):
        self.pizza = pizza
        self.cost = cost

    @abstractmethod
    def add_extra(self, ingridient):
        self.ingridient = ingridient
        print(f'{self.pizza} with extra {self.ingridient} costs {self.cost}')

# obj1 = Pizza('chilli', 1500)

class DodoPizza(Pizza):
    def add_extra(self, *ingridient):
        self.cost += 50 * len(ingridient)
        return super().add_extra(ingridient)

    @staticmethod
    def late(time):
        if time >= 5:
            print('You get free pizza card')

class PapaJohns(Pizza):
    def add_extra(self, *ingridient):
        self.cost += 70 * len(ingridient)
        return super().add_extra(ingridient)

    def late(self, time):
        if time >= 100:
            print(f'Your pizza is free')
        else:
            self.cost = self.cost - (self.cost * time/100)

    

pizza1 = DodoPizza('Pepperoni', 500)
pizza1.add_extra('cheese', 'sauce', 'pepperoni')
pizza2 = PapaJohns('Margarita', 400)
pizza2.add_extra('cheese', 'sauce', 'pepperoni')
pizza1.late(20)
pizza2.late(100)
pizza2.late(50)
print(pizza2.cost)
