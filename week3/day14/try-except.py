# Type of errors:

# 1) SyntaxError (forgot to write : (), wrote a wrong variable name)
# print(
# 2age = 2

# 2) IndentationError - wrong tab
    # 2

# 3) TabError - wrong tab (mix of tabs and gap)
# if True:
#     print('f1')
#     print('f2')




#  ИСКЛЮЧЕНИЯ / EXCEPTIONS

### ZeroDivisionError 
# print(2 / 0)

### NameError - name not defined
# name

### TypeError 
# res = 2 + '2'   # unsupported operand type for ...

### ValueError - тип обьекта подходит для операции, но его значение нет
# a = '2'
# b = 'abc'
# c = '1.5'
# g = 1.5
# print(int(c), int(b))

### IndexError - обращение к несуществующему индексу
# a = [1,2,3]
# print(a[3])

### KeyError -  обращение к несуществующему ключу
# dct = {'a': 2}
# print(dct['b'])

### ImportError
# from math import pi2

### ModuleNotFoundError - cannot fing module for import
# import math2

### AttributeError - вызов несуществующего атрибута/метода у объекта
# a = 'Hello'
# a.append('f')

### KeyboardInterrupt - breaking a cycle with Ctrl+C
# while True:
#     print('hello')



############################################################################
# ОБРАБОТКА ИСКЛЮЧЕНИЙ. ОПЕРАТОРЫ try-except
# try:
#     pass #try to do smth
# except:
#     pass #if an exception occurs process it


# try:
#     print(name)
#     2 / 0
# except: # голое исключение
#     print('No such varaible.')


# try: 
#     print(name)
#     2 / 0
# # except NameError:
# #     print('No such variable')
# # except ZeroDivisionError:
# #     print('Cannot divide by 0')
# except (ZeroDivisionError, NameError):
#     print('Cannot divivde by zero or no such variable')


# try:
#     age = int(input('Enter your age: '))
# except ValueError:
#     print('Enter numbers!')
#     age = int(input('Enter your age: '))


# num1 = 10
# num2 = 0
# try:
#     res = num1 / num2
# except ZeroDivisionError:
#     res = 0
# print(f'Result equals {res}')
# # print(res)

# try:
#     while True:
#         print('Hello')
# except KeyboardInterrupt:
#     print('end')


# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     res = num1 / num2
#     print(res)
# except(ZeroDivisionError, ValueError):
#     print('You have entered wrong values!')


# When type of error occured is unknown
# try:
#     num1 = int(input('Enter first number: '))
# except Exception as e:
#     print(e)
# print('hellooooo')


# try:
#     print(name)
# except:
#     print('NameError')
# else:
#     print('Если не сработал')
# finally:
#     print('Harry Potter')


########################################################################
# raise Exception - генерирование своей ошибки
# age = int(input('Enter your age: '))
# if age < 18:
#     raise ValueError('You are too young!')



# try:
#     age = int(input('Enter your age: '))
#     if age < 18:
#         raise ValueError('ffffffffffffff')
# except ValueError:
#     print('Your are too young!')


# scores = {'Timur': {'history': 90, 'math': 95, 'literature': 91},'Olga': {'history': 92, 'math': 96, 'literature': 81},'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# a = {k1:k2 for k1, v1 in scores.items() for k2, v2 in v1.items() if v2 == max(v1.values())}
# print(a)


try:
    age = int(input('Please enter your age: '))
    if age < 18:
        raise Exception
except ValueError:
    print('You have entered your age incorrectly.')
except Exception:
    print('Access denied.')
else:
    print('Thank you!')
finally:
    print('Goodbye!')