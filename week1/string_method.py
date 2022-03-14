# ЗАМЕНА СТРОКИ ПО ШАБЛОНУ
#string.replace(шфблон, замена, [max count])
# s = 'Hello world'
# result = s.replace('lo', 'dnf')
# print(result)


#SPLIT - РАЗДЕЛЕНИЕ СТРОКИ ПО ШАБЛОНУ, ПО УМОЛЧАНИЮ ПРОБЕЛ
#string.split(символ)
# s = 'summer#top#sport'
# print(s.split('#'))


#ISDIGIT - ПРОВЕРЯЕТ СОСТОИТ ЛИ СТРОКА ТОЛЬКО ИЗ ЧИСЕЛ (True/False)
#string.isdigit()
# s = '123 a' - false
# print(s.isdigit())


#ISALPHA - ПРОВЕРЯЕТ СОСТОИТ ЛИ СТРОКА ПОЛНОСТЬЮ ИЗ БУКВ
#string.alpha()
# s = 'hello'
# print(s.isalpha())


#ISALNUM - ПРОВЕРЯЕТ СОСТОИТ ЛИ СТРОКА ИЗ БУКВ ИЛИ/И СИМВОЛОВ, ВСЕ КРОМЕ СИМВОЛОВ
#string.isalnum() 
# s = 'world!55'
# print(s.isalnum())


#ISLOWER - ПРОВЕРЯЕТ, ЧТОБЫ ВСЕ СИМВОЛЫ СТРОКИ БЫЛИ В НИЖНЕМ РЕГИСТРЕ
#string.islower()
# s = 'hello '
# print(s.islower())

#ISUPPER - ПРОВЕРКА НА ВЕРХНИЙ РЕГИСТР
#string.isupper()
# s = 'HELLO WORLD'
# print(s.isupper())


#ISSPACE - ПРОВЕРКА СТРОКИ НА ПРОБЕЛ / НЕОТОБРАЖАЕМЫЕ СИМВОЛЫ
#s.isspace()
# s = ' \n'
# print(s.isspace())


#ISTITLE - НАЧИНАЮТСЯ ЛИ ВСЕ СЛОВА В СТРОКЕ С ЗАГЛАВНОЙ БУКВЫ
#string.istitle()
# s = 'Hello World'
# print(s.istitle())


#UPPER - ПРЕОБРАЗОВАНИЕ СТРОКИ К ВЕРХНЕМУ РЕГИСТРУ
#string.upper()
# s = 'Hello world!'
# print(s.upper())


#LOWER - ПРЕОБРАЗОВАНИЕ СТРОКИ К НИЖНЕМУ РЕГИСТРУ
#string.lower()
# s = input('Enter some word: ')
# print(s.lower())


# s.startswith() - НАЧИНАЕТСЯ ЛИ СТРОКА С КАКОГО-ЛИБО ШАБЛОНА
# s = '1hello world'
# print(s.startswith('1hello'))


# input() -> 3.startswith('3') -> int('3')


# s.endswith() - ЗАКАНЧИВАЕТСЯ ЛИ СТРОКА КАКИМ-ЛИБО ШАБЛОНОМ
# s = 'hello world'
# print(s.endswith('rld'))


# s.capitalize() - ПЕРЕВОДИТ ТОЛЬКО ПЕРВЫЙ СИМВОЛ В ВЕРХНИЙ, А ВСЕ ОСТАЛЬНЫЕ В НИЖНИЙ РЕГИСТР
# s = 'hello world'
# print(s.capitalize())
# print(s.title()) - ПЕРВЫЙ СИМВОЛ КАЖДОГО СЛОВА ПЕРЕВОДИТ К ВЕРХНЕМУ РЕГИСТРУ, А ОСТАЛЬНЫЕ К НИЖНЕМУ


# in string  - ПРОВЕРКА НА СОДЕРЖАНИЕ ШАБЛОНА
# s = 'hello'
# print('el' in s)


# s.swapcase() - ПЕРЕВОДИТ ВЕРХНИЙ РЕГИСТР В НИЖНИЙ, И НАОБОРОТ
# s = 'heLLo WorlD'
# print(s.swapcase())


# s.count(str, [start], [end]) - ПОДСЧЕТ ШАБЛОНА В СТРОКЕ. ПО УМОЛЧАНИЮ ВСЯ СТРОКА
# s = 'super some string'
# print(s.count('s', 0, 7))


# s.lstrip([chars]) - УДАЛЕНИЕ ПРОБЕЛЬНЫХ СИМВОЛОВ В НАЧАЛЕ СТРОКИ
# s = 'hhello'
# print(s.lstrip())
# print(s.lstrip('h'))


# # s.rstrip([chars]) - УДАЛЕНИЕ ПРОБЕЛОВ/ШАБЛОНА С КОНЦА СТРОКИ
# s = 'hhello'
# print(s.rstrip())
# print(s.rstrip('lo'))


# s.strip([chars}) - УДАЛЕНИЕ ПРОБЕЛЬНЫХ СИМВОЛОВ В НАЧАЛЕ И КОНЦЕ СТРОКИ
# s = 'hhelloh '
# print(s.strip())
# print(s.strip('h'))


# s.zfill(width) - СТРОКА НЕ МЕНЬШЕ ДЛИНЫ width, В ПРОТИВНОМ СЛУЧАЕ ЗАПОЛНИТ 0
# s = input('Enter some word: ')
# print(s.zfill(15))


# TASK - EMAIL, PASSWORD CHECK
# email = input('Enter email: ')
# if email.endswith('@gmail.com') or email.endswith('@email.com'):
#     password = input('Enter password: ')
#     password_confirmation = input('Enter password confirmmation: ')
#     if password == password_confirmation:
#         print('You have successfuly registered!')
#     else:
#         print('Passwords do not match!')
# else:
#     print('Email is not valid.')


data = 10500
key = 90
s = data^key
print(s)


import random
import string
a = ''
a = ''.join(random.choice(string.ascii_uppercase + 
string.ascii_uppercase + string.digits + string.punctuation) for i in range(10))
print(a + '1')
