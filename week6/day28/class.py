# class A:
#     def hello(self):
#         print('Hello, I\'m class A')

# class B(A): # дочерний класс
#     def hello(self):
#         print('Hello, I\'m class B')

# class C(B):
#     def hello(self):
#         print('Hello, I\'m class C')

# obj_a = A()
# obj_b = B()
# obj_c = C()

# for obj in [obj_a, obj_b, obj_c]:
#     obj.hello()

########################################################

# super() - вытаскивает метод родителя в дочернем классе
# class A:
#     def hello(self):
#         print('Hello, I\'m class A')

# class B(A):
#     def hello(self):
#         # super(B, self).hello() # метод родителя, устаревшая запись
#         super().hello()
#         print('Hello, I\'m class B')

# obj_b = B()
# obj_b.hello()

########################################################

# class Person:
#     def __init__(self, name, last_name, id_num):
#         self.n = name
#         self.l = last_name
#         self.i = id_num 

#     def get_info(self):
#         print(f'{self.n} {self.l} {self.i}')

# class Employee(Person):
#     def __init__(self, name, last_name, id_num, position, salary):
#         self.s = salary
#         self.p = position
#         super().__init__(name, last_name, id_num)

#     def get_full_info(self):
#         super().get_info()
#         print(f'{self.s} {self.p}')
        
# empl1 = Employee('Jack', 'Jackson', 100, 'IT specialist', 50000)
# empl1.get_full_info()

########################################################

# static methods
# issubclass.isinstance

# class Animal:
#     animal_sound = 'Aaaaaaaaa'
#     def sound(self):
#         return self.animal_sound

# class Cat(Animal):
#     animal_sound = 'Meow'

#     @staticmethod # оборачивает функцию 
#     def sound():
#         return 'Meow'

#     @staticmethod
#     def say_name(name):
#         print(name)

# cat = Cat()
# print(cat.sound())
# cat.say_name('Barsik')

# class HomeCat(Cat):
#     pass

# class Lion(Cat):
#     animal_sound = 'Roar'

# print(issubclass(Cat, Animal)) # проверка является ли первая функция дочерней для второй
# print(isinstance(cat, Animal)) # является ли cat экземпляром класса Animal

########################################################

class CheckUser():
    
    def __init__(self, username, age, password):
        self.n = username
        self.a = age
        self.p = password

    def check_age(self):
        if self.a >= 18:
            return True

    def check_password(self):
        if not self.p.isalnum() or self.p.isdigit():
            print('Password must contain letters and numbers!')
            return False
        else:
            print('Successfully registered!')
            return True
    
    def check_user_in_list(self):
        name = input('Enter name: ')
        if name in [i['username'] for i in self.users]:
            return True
        else:
            return False
        

class LoginOrRegisterUser(CheckUser):
    users = []

    def __init__(self, username, age, password):
        self.login = False
        super().__init__(username, age, password)

    def register_user(self):
        if super().check_password():
            user = {
                'username': self.n,
                'age': self.a,
                'password': self.p,
                'login': self.login
            }
            self.users.append(user)
            print('Successfully registered!')

    def login_user(self):
        if super().check_user_in_list():
            for user in self.users:
                if user['username'] == self.n:
                    user['login'] = True
            print('Successfull login!')
            print(self.users)
        else:
            print('No such user!')

    def get_users_list(self):
        print([i['username'] for i in self.users])

    def mailing(self):
        if super().check_age() and super().check_user_in_list():
            print('Mailing has been done!')
        else:
            print('Mailing is not available.')


user_jack = LoginOrRegisterUser('Jack', 30, 'pass123')
user_jack.register_user()
# user_jack.login_user()
# user_jack.get_users_list()
user_jack.mailing()