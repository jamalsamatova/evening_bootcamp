# Композиция

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
#     def get_total(self):
#         return self.pay * 12
# class Employee:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)
#     def total_salary(self):
#         return f'Total salary: {self.salary.get_total() + self.bonus}'
    
# obj = Employee(200, 100)
# print(obj.total_salary())

####################################################################

# class Engine:
#     def __init__(self, vol):
#         self.volume = vol
#     def get_fuel(self):
#         if self.volume == 2:
#             print('Расход: 10л/100км')
#         elif self.volume == 3:
#             print('Расход: 15л/100км')
#         elif self.volume == 4:
#             print('Расход: 20л/100км')
# class Car:
#     def __init__(self, name, vol):
#         self.name = name
#         self.vol = vol
#         self.engine = Engine(self.vol)
#     def get_info(self):
#         self.engine.get_fuel()
#         print(f'Name is: {self.name}')
# obj = Car('BMW', 3)
# obj.get_info()

###################################################################################################
# Агрегация

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
#     def get_total(self):
#         return self.pay * 12
# class Employee:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#     def total_salary(self):
#         return f'Total salary: {self.pay.get_total() + self.bonus}'
# salary = Salary(200)
# employee = Employee(salary, 100)
# print(employee.total_salary())

####################################################################

# class Engine:
#     def __init__(self, vol):
#         self.volume = vol
#     def get_fuel(self):
#         if self.volume == 2:
#             print('Расход: 10л/100км')
#         elif self.volume == 3:
#             print('Расход: 15л/100км')
#         elif self.volume == 4:
#             print('Расход: 20л/100км')
# class Car:
#     def __init__(self, name, vol):
#         self.name = name
#         self.vol = vol
#     def get_info(self):
#         self.vol.get_fuel()
#         print(f'Name is: {self.name}')
# obj_eng = Engine(4)
# obj = Car('BMW', obj_eng)
# obj.get_info()

###################################################################################################

# Принципы ООП
#1 Полиморфизм
#2 Инкапсуляция
#3 Абстракция
#4 Композиция
#5 Наследование
#6 Агрегация

###################################################################################################

# from abc import ABC, abstractclassmethod, abstractmethod
# class Salary:
#     @abstractmethod
#     def get_salary(self):
#         pass
# class IT(Salary):
#     def get_salary(self, salary):
#         print(f'My salary is {salary}')
# class HR(Salary):
#     def get_salary(self, salary):
#         print(f'My salary is {salary}')
#     pass
# obj_it = IT()
# obj_it.get_salary(200)
# obj_hr = HR()

###################################################################################################

# class Info:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password
#     @property
#     def password(self):
#         verification = input('Enter your password: ')
#         if verification == self.__password:
#             return f'User info: {self.name}, {self.__password}'
#         else:
#             return 'Wrong password!'
#     @password.setter
#     def password(self, new_password):
#         self.__password = new_password

# jamal = Info('Jamal', '123')
# jamal.password = 4
# print(jamal.password)

###################################################################################################

# class NewFile:
#     def __init__(self, name, ):
#         self.name = name
#     def write_data(self):
#         with open(f'{self.name}', 'a') as f:
#             while True:
#                 answer = input('Write? yes or no: ')
#                 if answer == 'yes':
#                     text = input('Enter text/data: ')
#                     f.write(text)
#                 else:
#                     break
#     def read_data(self):
#         with open(f'{self.name}', 'r') as f:
#             f.seek(0)
#             print(f.read())
# f = NewFile('test.txt')
# f.write_data()
# f.read_data()

###################################################################################################

class Lift:
    floor = 1
    def get_curr_fl():
        return f'Your are currently on {Lift.floor} floor.'

    def up_one():
        if Lift.floor + 1 <= 20:
            Lift.floor += 1
            return f'You are currently on {Lift.floor} floor.'
        else:
            return 'There are no more than 20 floors in the building!'

    def down_one():
        if Lift.floor - 1 >= 1:
            Lift.floor -= 1
            return f'You are currently on {Lift.floor} floor.'
        else:
            return 'The building starts with 1 floor!'

    def up(floors):
        if Lift.floor + floors <= 20:
            for i in range(1, floors+1):
                Lift.floor += 1
                print(f'You are currently on {Lift.floor} floor.')
                if Lift.floor + floors == 20:
                    break
                return Lift.floor
        else:
                print('There are no more than 20 floors in the building!')

    def down(floors):
        if 1 <= Lift.floor - floors:
            for i in range(1, floors + 1):
                Lift.floor -= 1
            print(f'You are currently on {Lift.floor} floor.')
        else:
            print('The building starts with 1 floor!')
        return Lift.floor
   

lift = Lift
print(lift.get_curr_fl())
# print(lift.up_one())
# print(lift.down_one())
lift.up(7)
# print(lift.down(4))
# print(lift.get_curr_fl())
