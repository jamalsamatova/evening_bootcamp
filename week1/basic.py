# print('Hello ' + 'world!')
# print('Hello\n' * 5)
#\n - перенос
# print('I\'m 25 years old')
#при помощи \ можно поставить кавычки в тексте
#print('John'[1:3])
#string[start : stop(не включительно) : step] - срез
#[:n] 0:(n-1)
#[1:] - все кроме первой
#[:] - от начала до конца
#[::-1] - наоборот
# [::2] - через один шаг от начала до конца

# print(len('Hello, John'))
# #len - величина строки (включает пробелы)
# string = 'Hello world'
# print(len(string))

# name = input('Enter your name ')
# surname = input('Enter your surname ')
# year = int(input('Please enter your year of birth '))
# message = 'Hello, ' + name + ' ' + surname + '. You are ' + str(2021 - year) + '!'
# print(message)
# ЧЕРЕЗ f СТРОКУ
# message_with_format = f'Hello {name} {surname}. You are {2021 - year}!'
# print(message_with_format)

# age = int(input('Please enter you age: '))
# if age >= 18 and age<= 50:
#     print('You can come in!')
# else:
#     print('You cannot enter')

# CYCLE
# some_str = 'Hello, world!'
# for i in some_str:
#     print(i)

# import math
# print(math.factorial(5))

# import random
# print(random.randint(1,100))

# string = 'hello'
# print(string[-2:])


string = 'The quick brown fox jumps over the lazy dog'
result = ''
for i in string:
    if i == 'o':
        i = '*'
    result += i
print(result)


string = 'desktop'
result = ''
for i in string:
    if i == 'string[0]':
        i = 'string[-1]'
    if i == 'string[-1]':
        i = 'string[0]'
    result += i
print(result)