# ООП - подход решения задач в программированиис помощью классов, объектно ориентированное програмирование (парадигма какая-то)
# Класс - 
# Объявление класса:
# class A: # название класса должно быть через CamelCase
#     string = '' # переменная класса - переменная, находящаяся с каком-либо классе
#     # Методы
#     def first_method(self): #все методы внутри класса первым аргументом принимают self
#         pass 
# first_obj = A() # создали экземпляр/объект от класса А
# second_obj = A() 

########################################################

# class Animal:
#     def __init__(self, name, animal_type): # магический метод __init__ не нуждается в вызове
#         # инит нужен для инициализации
#         self.name = name # атрибут объекта
#         self.animal_type = animal_type # из объекта вытащи вид
    
#     # Метод объекта
#     def get_info(self): # self является ссылкой на объект
#         print(f'Name is {self.name}, type is {self.animal_type}')

# dog = Animal('Baks', 'Dog')
# cat = Animal('Barsik', 'Cat')

# dog.get_info()
# cat.get_info()

# print(dog.name) # достаем атрибут объекта

########################################################

# class People:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

#     def get_info(self):
#         print(f'Hello, I\'m {self.name}')

#     def translate_hello(self, hello):
#         print(f'Country is {self.country}, in my country "hello" is "{hello}"')

# american = People('Tom', 'USA')
# kyrgyz = People('Aibek', 'KG')
# russian = People('Ivan', 'Russia')

# american.get_info()
# kyrgyz.get_info()
# russian.get_info()

# # так как метод перевода имеет параметр приветствия, необходио вписать его при вызове функции в аргумент
# american.translate_hello('Hello')
# russian.translate_hello('Привет')
# kyrgyz.translate_hello('Салам')

########################################################

# class SelfBank:
#     total = 0

#     def add_summ(self, sum_):
#         self.total += sum_
#         return self.total
    
#     def get_total_summ(self):
#         return self.total
    
#     def minus(self, sum_):
#         if self.total - sum_ < 0:
#             print('Not enough money')
#             return self.total
#         self.total -= sum_
#         return self.total

# john = SelfBank()
# print(john.get_total_summ())
# john.add_summ(1000)
# john.minus(250)
# john.minus(1000)
# print(john.get_total_summ())
# john.total

# jessica = SelfBank()
# jessica.total

########################################################

class Car:
    car_cnt = 0
    def __init__(self):
        Car.car_cnt += 1
car1 = Car()
print(car1.car_cnt)
car2 = Car()
print(car1.car_cnt)

########################################################

# class A:
#     def method1(self):
#         print('Hello')
# obj_a = A()
# print(obj_a.__dir__())
# print(dir(obj_a))

########################################################

# class Calculator:

#     def plus(self, value1, value2):
#         print(value1 + value2)

#     def minus(self, value1, value2):
#         print(value1 - value2)

#     def divide(self, value1, value2):
#         print(value1 / value2)

#     def multiply(self, value1, value2):
#         print(value1 * value2)

# result = Calculator()

# result.plus(5, 8)
# result.minus(17,6)


############################## РЕКУРСИЯ ##############################

def factorial_recursive(n):
    if n == 1: #точка выхода
        return n
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(7))
