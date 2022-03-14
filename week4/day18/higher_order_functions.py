#  lambda - alternative shorter writing of a function
# def add_nums(a,b):
#     return a + b
# result = add_nums(5,10)
# print(result)
# result = lambda a, b: a + b
# print(result(10,20))

###################################################################

# map() - ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА ДЛЯ ПРИМЕНЕНИЯ ФУНКЦИИ КАЖДОМУ ЭЛЕМЕНТУ В ИТЕРИРУЕМОМ ТИПЕ
# lst = [1, 2, 3, 4, 5]
# result = list(map(lambda x: str(x), lst))
# def do_str(x):
#     return str(x)
# result = list(map(do_str, lst))
# print(result)

###################################################################

# filter()
# lst = [1,2,3,4,5,6,7,8,9,10]
# result = list(filter(lambda x: x > 5, lst))
# def filter_this(x):
#     return x > 5
# result = list(filter(filter_this, lst))
# print(result)
# !!! функция должна принимать и возвращать только один элемент

###################################################################

# reduce() - возвращает только одно значение
# from functools import reduce
# lst = [1,2,3,4,5]
# result = reduce(lambda x, y: x + y, lst)
# def summ_this(x,y):
#     return x + y
# result = reduce(summ_this, lst)
# print(result)

####################################################################

# zip() - возвращает список из кортежей
employee_numbers = [2,9,18,28]
employee_names = ['Helen', 'Sam', 'Jessica', 'James']
employee_spheres = ['IT', 'Broker', 'Cook', 'Banker']
zipped_values = zip(employee_numbers, employee_names, employee_spheres)
zipped_list = list(zipped_values)
print(zipped_list) 

####################################################################

# lst = [1,2,3,4,5,6,7,8,9,10]
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', lst))
# def nums(x):
#     return 'even' if x % 2 == 0 else 'odd'
# result = list(map(nums, lst))
# print(result)

####################################################################

# CRUD - create, read, update, delete
#{'Tom': 'pass123'}
# dct = {}
# def manager():
#     choice = input('Enter what action do you want to do (c,r,u,d): ')
#     if choice == 'c':
#         create()
#     elif choice == 'r':
#         read()
#     elif choice == 'u':
#        update()
#     elif choice == 'd':
#        delete()
#     else:
#         print('Enter c, r, u or d!')

# def create():
#     global dct
#     name = input('Enter your name: ')
#     password = input('Enter your password: ')
#     dct[name] = password
#     print(f'Successfully created: {dct}.')
#     manager()

# def read():
#     print(f'Users list: {dct.keys()}.')
#     manager()

# def update():
#     global dct
#     name = input('Enter your name: ')
#     if name in dct.keys():
#         new_password = input('Enter your new password: ')
#         dct[name] = new_password
#         print(f'Successfully changed {name}.')
#     else:
#         print('User not found. Register!')
#         create()
#     manager()

# def delete():
#     global dct
#     name = input('Enter your name: ')
#     old_password = input('Enter your old password: ')
#     if old_password == dct[name]:
#         dct.remove(name)
#     else:
#         print('Incorrect password.')
#     manager()

# manager()

# rafael = [1, 0, 3]
# novak = [2, 2, 1]
# scores = zip(rafael,novak)
# def winneris(lst, name1, name2):
#     s1 = 0
#     s2 = 0
#     for score1, score2 in (lst):
#         if score1 > score2:
#             s1 += 1
#         elif score2 > score1:
#             s2 += 1
#     dct2 = {name1: s1, name2: s2}
#     for k, v in dct2.items():
#         if v == max(dct2.values()):
#             winner = k
#     print(f'The winner of the game is {winner} with final score {max(dct2.values())}:{min(dct2.values())}.')

    
# winneris(scores, 'rafael', 'novak')

