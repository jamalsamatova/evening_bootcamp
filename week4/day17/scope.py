# import random
# rand_num = random.randint(1,11)
# attempts = 3
# def check_attempts():
#     if attempts == 0:
#         print('You have no more attempts.')
#         return False
#     return True

# while check_attempts():
#     print(f'Try to guess the number given for computer, you have {attempts} attempts left.')
#     num = int(input('Enter your number: '))
#     attempts -= 1
#     if num == rand_num:
#         print('Congratulations! You have guessed the right number!')
#         break
    



# accounts = [[4329338,6323984,9298227],[287363,293873,88463],[2874,87663,7366782]]


# def richest(lst): 
#     list_of_balances = []
#     for account in lst:
#         balance = sum(account)
#         list_of_balances.append(balance)
#     return max(list_of_balances)
# print(richest(accounts))

# Области видимости
# LEGB - Local enclosed global built - in

################################################
# x = 'Это глобальная переменная'

# def f():
# x = 'Локальная (enclosed) переменная'
# print(x)
# def f2():
# x = 'Локальная переменная 2'
# print(x)
# return f2()
# print(x)
# f()
################################################

# locals(), globals() возвращают словарь

# x = 'Hello'
# def f():
# print('Hello')
# # print(globals())
# # print(x is globals()['x'])
# globals()['new_data'] = 'Some data'
# print(globals())

################################################

# def f():
# x = 'Hello'
# locals()['y'] = 525
# # print(locals())
# def f2():
# x = 100
# print(locals())
# return f2()
# f()

################################################

# def counter():
# counter = 0
# counter += 1
# print(counter)

# counter()
# counter()
# counter()


# counter = 0
# def counter_():
# global counter
# counter += 1
# print(counter)

# counter_()
# counter_()
# counter_()

################################################

# nonlocal

# def f():
# x = 20
# def g():
# nonlocal x
# x = 40
# g()
# print(x)
# f()

################################################

# def manager():
# f()

# def f():
# print('hello world')

# manager()

################################################

# CRUD - create read/retrieve update delete
# просто пример:
# def create():
# logic
# create succsess
# manager()

# def manager():
# create? -> y
# create()
################################################

# Чистая функция должна быть детерминированной и без побочек

# детерминированная функция
# def sum(a,b):
# return a + b
# print(sum(3, 6))
# print(sum(3, 6))

# недетерминированная функция
# import random
# print(random.random())
# print(random.random())
# print(random.random())


# lst = [32,3,50,2,29,43]
# def sort_by_sort(li):
# li.sort()
# print(li)
# sort_by_sort(lst)
# print(lst) # список изменился (функция имеет побочные эффекты)


# lst = [32,3,50,2,29,43]
# def sort_by_sort(li):
# print(sorted(li))
# return sorted(li)

# sort_by_sort(lst)
# print(lst) # список не изменился (функция не имеет побочные эффекты)

################################################

# ФВП - функции высшего порядка

# def func(num):
# return num ** 2

# def fvp_func(fun, num):
# return fun(num) + fun(num)

# print(func(4))
# print(fvp_func(func, 5))


#######################################################
# ПРОСТРАНСТВО ИМЕН

# Встроенное пространство buit-ins
# dir(__builtins__)
# Глобальное пространство global
# Замкнутое пространство enclosed
# Локальное пространство local

# this_var_is_visible = 'You can see me indside and outside the function'
# def var_visibility():
#     this_var_is_not_visible = 'You can see me only inside the function'
#     print(this_var_is_not_visible)
#     print(this_var_is_visible)
# # print(this_var_is_visible)
# var_visibility()


# word  = "I'm global"
# def func_a():
#     word = "I'm local"
#     print(word)
# func_a()
# print(word)


# word = "I'm global"
# def outer():
#     word = "I'm enclosed"
#     print(word)

#     def inner():
#         word = "I'm local"
#         print(word)

#     inner()

# outer()
# print(word)

# name = 'Makers'
# print(globals())
# print(locals())

# globals()['name'] = 'Bootcamp'


# def func(company):
#     name = 'Bootcamp'
#     print(locals())
# func(company = 'Makers')

# параметры функции являются локальными для данной функции


# def info(name, age, height):
#     name = 'Alice'
#     age = 30
#     print(locals())
# info(name = 'Carley', age = 25, height = 165)
# print(locals())


# x = 20
# def func():
#     global x
#     x = 40
#     print(x)

import datetime
print(int(datetime.datetime.now().month))