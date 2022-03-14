# СЛОВАРИ - ИЗМЕНЯЕМЫЙ, УПОРЯДОЧЕННЫЙ, ИТЕРИРУМЫЙ ТИП ДАННЫХ
# Ключ должен быть неизменяемым типом данных!!!
# dct = {}
# print(type(dct))

# синтаксис {key1: value, key2: value, ...}
# dct = {'name': 'John', 'age': 25, 'hobby': ['fishing', 'football', [1,2,3]]}
# print(dct['hobby'])

# dct = dict([[1,2]])
# print(dct)

# dct = dict(name = 'John')
# print(dct)


# МЕТОДЫ СЛОВАРЕЙ
# dct = {'name': 'John', 'age': 25, 'hobby': ['fishing', 'football', [1,2,3]]}

# dict.clear() - очищает словарь
# dct.clear()
# print(dct)


# dct2 = dct #ссылаются на одну ячейку памяти => при изменении одного словаря, изменяется другой
# print(dct2)
# print(dct)
# dct2['name'] = 'John2'
# print(dct2)
# print(dct)
# TO DETERMINE THE ID: id(dict)

# dict.copy() - поверхностное копирование, вложенный списки/кортежи относятся к одному id
# dct2 = dct.copy()
# print(dct)
# print(dct2)
# dct2['name'] = 'John2'
# dct['hobby'][0] = '2'
# print(dct)
# print(dct2)


# dict.deepcopy() - глубокое копирование
# import copy
# dct2 = copy.deepcopy(dct)
# print(id(dct['hobby']))
# print(id(dct2['hobby']))


# dict.fromkeys() - создает словарь с ключом(-ами) и значением, по умолчанию ключу присваевается None
# list_ = ['a', 'b', 'c']
# dct = dict.fromkeys(list_, 'John')
# print(dct)


# dict.get() - получение значения по ключу, если нет ключа -> None
# dct = {'name': 'John', 'age': 25}
# print(dct.get('name'))
# print(dct.get('hi', 'No such key'))


# dict.values() - возвращает все значения словаря
# dct = {'name': 'John', 'age': 25}
# print(dct.values())


# dict.keys() - вощвращает все ключи словаря
# dct = {'name': 'John', 'age': 25}
# print(dct.keys()) 


# dict.items() - вощвращает все элементы (ключи и значения) словаря
# dct = {'name': 'John', 'age': 25}
# print(dct.items()) 


# dct = {'name': 'John', 'age': 25}
# for key, value in dct.items():
#     print(key)
#     print(value)


# dict.pop(ключ, [в случае, если ключа не существует]) - удаляет элмент по ключу и возвращает его значение
# dct = {'name': 'John', 'age': 25}
# k = dct.pop('name')
# print(k)
# print(dct)


# dict.popitem - удаляет последний элемент, возвращая его 
# k = dct.popitem()
# print(k)


# dict.setdefault() - возвращает значение ключа. Если нет такого ключа, не выдавая ошибку, создает ключ со значением (по умолчанию None)
# dct = {'name': 'John', 'age': 25}
# k = dct.setdefault('name2', 'Harry')
# print(k)
# print(dct)


# dict.update({key:value}) - обновление словаря (перезапишет, если ключ сущесвует)
# dct = {'name': 'John', 'age': 25}
# dct.update({'surname':'Snow', 'age2': 26})
# print(dct)

# i = 0
# while i < len(dct):
#     k = list(dct.keys())[i]
#     print(k)
#     print(dct[k])
#     i += 1


# dct = {'a': 19, 'b': 20, 'c':5, 'f': 30}
# for key, value in dct.items():
#     if value % 2 == 0:
#         dct.update({key: 'yes'})
#     else:
#         dct.update({key: 'no'})
# print(dct)


# HOMEWORK
'''
1. Создайте словарь и выведите один из ключей.
'''
from typing import Dict


dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
print(list(dct.keys())[0])
'''
2. Создайте словарь с любыми элементами, удалите один из элементов и распечатайте удалённый элемент.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
deleted_item = dct.popitem()
print(deleted_item)
'''
3. Создайте словарь, добавьте в него новую пару ключ: значение и распечатайте.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
dct.update({'gender': 'female'})
print(Dict)
'''
4. Создайте словарь, удалите всего его элементы и распечатайте результат.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
dct.clear()
print(dct)
'''
5. Создайте словарь, выведите все его ключи.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
print(dct.keys())
'''
6. Создайте словарь, сделайте его копию и распечатайте её.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
dct2 = dct.copy()
print(dct2)
'''
7. Дан словарь, нужно перебрать его и распечатать все ключи.
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
for key in dct.keys():
    print(key)
'''
8. Создайте словарь, перебирите его и распечатайте все значения
'''
dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
for value in dct.values():
    print(value)
'''
9. Создайте словарь с числовыми значениями, пройдитесь по элементам и замените все чётные числа на число 2.
Пример: Ввод -> a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
        Вывод -> a{'a': 1, 'b': 2, 'c': 1, 'd': 5,  'e': 2}
'''
dct = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
for key, value in dct.items():
    if value % 2 == 0:
        dct[key] = 2
print(dct)
'''
10. Дан словарь, удалите из него все элементы с пустыми значениями.
Пример: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} ->
          {'b': 1, 'c': 2, 'e': 3}
'''
dct = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
lst = []
for key, value in dct.items():
    if value == None:
        lst.append(key)
for i in lst:
    dct.pop(i)
print(dct)
'''
11. Создайте словарь, где ключами будут названия товаров, а значениями их цены,  затем, его нужно перебрать циклом и поменяйте все значения элементов, разделив их на 5
'''
menu = {'Sandwich': 125, 'Latte': 130, 'Pizza': 220, 'Pancakes': 150, 'Tea': 99}
for food, price in menu.items():
    menu[food] = round(price / 5, 2)
print(menu)
'''
12. Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
'''
price_list = {'apples': 78, 'bananas': 115, 'tangerines': 191, 'kiwi': 176, 'oranges': 129}
lst = []
for fruit, price in price_list.items():
    if price % 2 == 0:
        lst.append(fruit)
for i in lst:
    price_list.pop(i)
print(price_list)
'''
13. Создайте словарь, а затем поменяйте местами ключи и значения. Распечайте полученный результат.
'''
# dct = {'picture': 'картина', 'book': 'книга', 'ant': 'муравей'}

'''
14. Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
'''
check = {'shorts': 5, 't-shirt': 9, 'dress': 23, 'jeans': 14, 'boots': 130, 'sneakers': 99}
total = 0
for price in check.values():
    total += price
print(f'The total purchase amount is ${total}.')
'''
15. Создайте словарь тремя возможными способами.
'''
dct1 = {}