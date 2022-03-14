# Магические методы - методы, срабатывающие сами под капотом без вызова

# class A:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, other): #при использовании знака плюс
#         print('ADD METHOD WORKED')
#         # self.num = 100
#         return self.num + other.num

#     def __sub__(self, other):
#         print('SUB METHOD WORKED')
#         return self.num - other.num     

#     def __gt__(self, other):
#         print('GREATER THAN METHOD WORKED')
#         return self.num > other.num 
    
#     def __lt__(self, other):
#         print('LESS THAN METHOD WORKED')
#         return self.num < other.num 

#     def __eq__(self, other):
#         print('EQUAL METHOD WORKED')
#         return self.num == other.num 

# obj1 = A(5)
# obj2 = A(15)
# print(obj1 + obj2) #объекты с объектами  складывать нельзя, НЕОБХОДИМО ЯВНО ПЕРЕДАТЬ МЕТОДЫ
# print(obj1 - obj2)
# print(obj1 > obj2)
# print(obj1 < obj2)
# print(obj1 == obj2)

#############################################################################################

# class C:
#     def __new__(cls, *args):
#         new_obj = object.__new__(cls)
#         print('C class __new__ is called')
#         return new_obj

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print('C class __init__ is called')

# obj = C('apple', 50)

#############################################################################################

# class B:
#     def __init__(self, data):
#         self.data = data

    # def __str__(self):
    #     return f'str method is called'

#     def __repr__(self):
#         return f'B({self.data!r})'
# obj = B('hello')
# print(obj.data)
# new_obj = eval(repr(obj))
# print(new_obj)

#############################################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __getattr__(self, name): # Вылавливает ошибку -  когда нет атрибута
#         print('GETATTR WORKED')

#     def __getattribute__(self, name):
#         print('GETATTRIBUTEE WORKED')
#         return super().__getattribute__(name)

# obj = Person('Tom', 30)
# print(obj.surname)

#############################################################################################

# class Som:
#     currencies = {
#         'USD': 84.5,
#         'EUR': 96,
#         'RUB': 1.1,
#         'KZT': 0.2,
#         'SOM': 1
#     }

#     def __init__(self, value, curr):
#         self.value = value
#         self.curr = curr

#     def __sub__(self, other):
#         curr1 = Som.currencies.get(self.curr)
#         curr2 = Som.currencies.get(other.curr)
#         print(f'{self.value * curr1} som {other.value * curr2} som')
#         return self.value * curr1 - other.value * curr2

# a = Som(100, 'USD')
# b = Som(50, 'EUR')
# print(a - b)

#############################################################################################

# class Distance:
#     units_M = {
#         'cm': 0.01,
#         'dm': 0.1,
#         'm': 1, 
#         'km': 1000,
#         'miles': 1600
#     }

#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit

#     def __gt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} m and {other.value *dist2} m')
#         return self.value * dist1 > other.value * dist2

#     def __lt__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} m and {other.value *dist2} m')
#         return self.value * dist1 < other.value * dist2

#     def __eq__(self, other):
#         dist1 = Distance.units_M.get(self.unit)
#         dist2 = Distance.units_M.get(other.unit)
#         print(f'{self.value * dist1} m and {other.value *dist2} m')
#         return self.value * dist1 == other.value * dist2

# a = Distance(1, 'km')
# b = Distance(10000, 'dm')
# print(a == b)

#############################################################################################

# class A:
#     def count(self, string):
#         vowels = 0
#         for i in string:
#             if i.lower() in 'eyuioa':
#                 vowels += 1
#         return vowels

# class B:
#     def count(self, string):
#         consonants = 0
#         for i in string:
#             if i.lower() in 'qwrtpsdfghjklzxcvbnm':
#                 consonants += 1
#         return consonants

# a = A()
# print(a.count('Hello'))
# b = B()
# print(b.count('Hello'))

#############################################################################################

# + --> __add__()
# - --> __sub__()
# * --> __mul__()
# / --> __div__()
# == --> __eq__()
# != --> __ne__()
# % --> __mod__()
# > --> __gt__()
# < --> __lt__()
# >= --> __ge__()
# <= --> __le__()

#############################################################################################

# class MyClass:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __setattr__(self, name, value):
#         print(f'I want to set attribute {name} with value {value}')
#         self.__dict__[name] = value

#     def __delattr__(self, name):
#         print(f'I want to delete attribute with name {name}')
#         return super().__delattr__(name)

#     def __getattr__(self, name):
#         pass

#     def __getattribute__(self, name):
#         return super().__getattribute__(name)

# obj = MyClass('John', 30)
# obj.surname = 'Snow'
# obj.__delattr__('age')
# print(obj.__dict__)