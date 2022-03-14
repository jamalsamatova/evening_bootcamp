# class A:
#     def hello(self):
#         print('Hello, class A')

# class B:
#     def hello(self):
#         print('Hello, class B')

# class C(A,B):
#     pass

# obj_c = C()
# obj_c.hello() # посик происходит слева направа (очередность важна)


# class MomParent():
#     def mom_parents_info(self):
#         print('Mom\'s parents')

# class DadParent:
#     def dad_parents_info(self):
#         print('Dad\'s parents')

# class Mom(MomParent):
#     def mom_info(self):
#         print('Mom')

# class Dad(DadParent):
#     def dad_info(self):
#         print('Mom')

# class Child(Mom, Dad):
#     def child_info(self):
#         print('Child')

# child = Child()
# child.mom_parents_info()
# child.dad_info()
# child.child_info()

###################################################################

# class.mro() - method resolution order (порядок разрешения метода)
# print(Child.mro())

###################################################################
# DIAMOND PROBLEM - проблема ромба - неправильный порядок поиска
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass

# obj = D()
# print(D.mro())

###################################################################

# class SoundMixin: # декоратор для класса - класс с общими функциями
#     # окончание на Mixin, ни от чего не наследуется, объекты не создавать

#     def sound(self):
#         print('Sound')

# class People(SoundMixin):
#     pass

# class Animal(SoundMixin):
#     pass

# class Car(SoundMixin):
#     pass

# people = People()
# animal = Animal()
# car = Car()

# for obj in [people, animal, car]:
#     obj.sound()

###################################################################

# class A:
#     def hello(self):
#         print('Hello class A')

# class B:
#     def helloB(self):
#         print('Hello class B')

# class C:
#     def hello(self):
#         print('Hello class C')

# вывод метода от определенного родителя
# class D(A,B,C):
#     def hello(self):
#         super().hello() # вызовет метод А
#         super().helloB() # метод В (уникальный метод в родителе В)
#         super(A, self).hello() # начинается поиск с класса А, который не включени => начнет с В
#         B.helloB(self)
#         print('Hello class D')

# obj_d = D()
# print(D.mro())
# obj_d.hello()

###################################################################

# task - CRUD{'name1': password1, 'name2': password2}

# class DataBase:

#     db = {}

#     def create(self, name, password):
#         self.db[name] = password
#         return self.db

#     def read(self):
#         return self.db

#     def update(self, name, new_password):
#         self.db[name] = new_password
#         return self.db

#     def delete(self, name):
#         self.db.pop(name)
#         return self.db

# j = DataBase()
# print(j.create('Jamal', '123'))
# print(j.read())
# m = DataBase()
# print(m.update('Meerim', '12'))
# m.delete('Meerim')
# print(j.read())

###################################################################

# class Ask:

#     def request(self):
#         link = input('which site? (vesti, enter, kivano): ')
#         import requests
#         if link == 'kivano':
#             response = requests.get('https://www.kivano.kg/')
#         elif link == 'enter':
#             response = requests.get('https://enter.kg/')
#         elif link == 'vesti':
#             response = requests.get('https://vesti.kg/')

#         choice = input('Status code or HTML? (s or h) ')
#         if choice == 's':
#             print(response.status_code)
#         else:
#             print(response.text)
# a = Ask()
# a.request()

###################################################################

# task2
class IdkMixin:
    @staticmethod
    def get_info():
        print('''Класс для просмотра информации о фильмах, доступны методы:
create_film - создание поста о фильме, 
get_all_films - получение списка всех фильмов
filter_films - фильтрует по категории фильмы, 
search films - поиск фильмов по седержанию или заголовку!''')


class Movie:
    db =  [
        {'title': 'Fast&Furios2', 'body': 'Film about cars', 'category': 'action', 'author': 'Admin', 'created_on': '2022-01-28'},
        {'title': 'Harry Potter', 'body': 'Film about Harry', 'category': 'fantastic', 'author': 'Admin', 'created_on': '2022-01-28'},
        {'title': 'Marvel', 'body': 'Film about Marvel', 'category': 'adventure', 'author': 'Admin', 'created_on': '2022-01-28'}
    ]

    def create_film(self):
        from datetime import datetime
        title = input('Enter title: ')
        body = input('Enter body: ')
        category = input('Enter category: ').lower()
        author = input('Enter author: ')
        time = datetime.datetime
        film = {
            'title': title,
            'body': body,
            'category': category,
            'author': author,
            'created_on': str(datetime.date(datetime.now()))
        }
        self.db.append(film)
        print('Movie successfully created!')


    def get_all_films(self):
        all_films = [i['title'] for i in self.db]
        print(all_films)
        

    def filter_films(self):
        category = input('Enter category: ')
        films = list(filter(lambda x: x['category'] == category, self.db))
        print(films)


    def search_films(self):
        search = input('Enter some word: ')
        films = list(filter(lambda x: search.lower() in x['title'] or search.lower() in x['body'], self.db))
        print(films)
