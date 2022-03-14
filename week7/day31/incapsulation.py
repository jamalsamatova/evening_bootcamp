# ИНКАПСУЛЯЦИЯ - объединение логически похожих данных в один класс и защита данных от воздействия пользователя
# реализована на уровне соглашения, к примеру для сохранения паролей

# class ClassName:
#     def __init__(self):
#         # модификаторы доступа
#         self.public_attr = 'Public attribute'
#         self._protected_attr = 'Protected attribute'
#         self.__private_attr = 'Private attribute'
#     def public_method(self):
#         print('Hello, public method')
#     def _protected_method(self):
#         print('Hello, protected method!')
#     def __private_method(self):
#         print('Hello, private method')
# obj = ClassName()
# print(obj.public_attr)
# print(obj._protected_attr)
# print(obj.__private_attr) # AttributeError
# obj.public_method()
# obj._protected_method()
# obj.__private_method() # AttributeError



#################################################################################

# getter и setter - методы посредники (получение и установление значений)
# class SomeClass:
#     def __init__(self):
#         self.__private_attr = 'Private attribute'
#         self.attr = 'Simple attribute'
#     def get_private_attr_info(self): # getter - посредник, имеющий доступ к приватному методу, тк он находится в классе
#         print('Return some private attribute')
#         return self.__private_attr
#     def set_private_attr(self, new_value): # setter method
#         print('I can help you to set a new value for private attribute')
#         self.__private_attr = new_value
#         return self.__private_attr
# obj = SomeClass()
# print(obj.get_private_attr_info())
# print(obj.attr)
# obj.attr = 'New value' # дали атрибуту новое значение (приватному атрибуту не присваивется!)
# print(obj.attr)
# print(obj.get_private_attr_info())
# print(obj.set_private_attr('NEW VALUE'))
# print(obj.get_private_attr_info())

#################################################################################

# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password
#     def get_user_info(self):
#         answer = input('Enter your password: ')
#         if answer == self.__password:
#             print(f'Username: {self.name}. Password: {self.__password}')
#         else:
#             print('Password is incorrect!')
#     def set_new_password(self):
#         answer = input('Do you actually want to change your password? (yes or no) ')
#         if answer == 'yes':
#             new_password = input('Enter new password: ')
#             self.__password = new_password
#             return self.__password
# obj = User('Helen', 'pass123')
# print(obj.name)
# obj.get_user_info()
# obj.set_new_password()
# obj.get_user_info()

#################################################################################

# class Geek:
#     def __init__(self, age = 0):
#         self.__age = age

#     def get_age(self):
#         return self.__age

#     @property
#     def set_age(self, value):
#         self.__age = value

# class Geek:
#     def __init__(self):
#         self.__age = 0
#     @property
#     def age(self):
#         print('Getter method called')
#         return self.__age
#     @age.setter
#     def age(self, new_age):
#         if new_age < 18:
#             raise ValueError('Sorry, age is bellow eligibility criteria')
#         print('Setter method called')
#         self.__age = new_age
# obj = Geek()
# obj.age = 25
# print(obj.age)

#################################################################################

# class Person:
#     def __init__(self, name, hours, per_hour):
#         self.name = name
#         self.hours = hours
#         self._per_hour = per_hour
#     @property # превращает функцию в атрибут
#     def salary(self):
#         try:
#             return self.__salary
#         except:
#             self.__salary = self.hours * self._per_hour
#             return self.__salary
#     @salary.setter
#     def salary(self, new_salary):
#         self.__salary = new_salary
# person1 = Person('Tom', 30, 15)
# print(person1.salary)
# person1.salary = 9000
# print(person1.salary)

#################################################################################

# ДЕКОРАТОРЫ
# @staticmethod - помогает использовать метод внутри класса, не принимая self(сам объект)
# @abstractmethod - помогает создать абстрактный метод, который в последующем обязательно должен быть переопределен в дочерних классах, иначе выведит ошибку
# @property - позволяет взаимодействовать с защищенным / приватным атрибутом через setter метод, вызывая его как атрибут
# @name.setter - похож на проперти, позволяет установить значение защищенному атрибуту (не работает без проперти!)
# @classmethod - позволяет сделать обычный метод методом класс, логика которого в последующем будет влиять на весь класс в целом (обычный метод класса, имеющий доступ ко всем атрибутам класса, через которыц он был создан) - метод, привязанный к классу, а не к экземпляру

#################################################################################

# from datetime import date
# class Person:
#     def __init__(self, name, year):
#         self.name = name
#         self.age = year
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
# obj1 = Person('TOm', 30)
# print(obj1.age)
# obj2 = Person.from_birth_year('Helen', 1995)
# print(obj2.age)

#################################################################################

# class Post:
#     posts = [] # [{smth, comments: []}, {...}, ...]
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.comments = []
#         self._add_to_posts()
#     @classmethod
#     def __generate_id(cls):
#         import random
#         id_ = random.randint(100, 1000)
#         for post in cls.posts:
#             if id_ == post.get('id'):
#                 return cls.__generate_id()
#         return id_
#     def _add_to_posts(self):
#         post = {
#             'id': Post.__generate_id(),
#             'title': self.title, 
#             'author': self.author,
#             'comments': self.comments
#         }
#         Post.posts.append(post)
#     def get_all_posts(self):
#         for post in self.posts:
#             print(post)
#     def add_comment(self, comment):
#         self.comments.append(comment)
#         print('Comment added!')
#     @property
#     def comments_cnt(self):
#         return len(self.comments)
# post1 = Post('Python', 'Jack')
# post2 = Post('HTML', 'Jessica')
# post3 = Post('JS', 'Helen')
# post1.add_comment('Good post')
# post1.get_all_posts()
# post1.add_comment('Awful!')
# print(post1.comments_cnt)
# post1.get_all_posts()