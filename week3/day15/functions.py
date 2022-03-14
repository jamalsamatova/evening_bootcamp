# def func1(a, b): #параметры
#     return a + b
# print(func1(2,1)) #аргументы
# Returns smth under any conition, if no 'return' -> None


# def  func1(a: int,b: int) -> int: 
#     res = a + b
#     return res
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(func1(num1, num2))


# optional argument
# def func_sum(a,b,c=2):
#     return a + b + c
# print(func_sum(3,28))


############ ПОЗИЦИОННЫЕ И ИМЕНОВАННЫЕ АРГУМЕНТЫ ############

# def func2(x,y):
#     return x * y
# print(func2(2, 3)) # позиционные аргументы
# print(func2(y = 2, x = 3))  # именованные аргументы
# ПОСЛЕ ИМЕННОВАННЫХ НУЖНО ВСЕГДА ПЕРЕДАВАТЬ ИМЕНОВАННЫЕ
# print(func2(2, y = 2)) 
# print(func2(y = 2, 8)) # ERROR


#################### *args, **kwargs #######################
# args - позиционные аргументы
# kwargs - именованные аргументы
# def func5(a,b ,*args, **kwargs):
#     print(a,b,args,kwargs)
#     print(a,b,*args,kwargs)
# func5(2,4,22,3,5,3,5,6,3, name = 'John')


# def sum_(a,b):
#     return a + b
# def dif_(a,b):
#     return a - b
# def multi_(a,b):
#     return a * b
# def div_(a,b):
#     return a / b

# while True:
#     start = input('Do you want to start? (yes or no): ')
    
#     if start == 'no':
#         break
#     elif start == 'yes':
#         num1 = int(input('Enter first number: '))
#         operation = input('Enter + - * /: ')
#         num2 = int(input('Enter second number: '))
    
#         if operation == '+':
#             print(sum_(num1,num2))
#         elif operation == '-':
#             print(dif_(num1,num2))
#         elif operation == '*':
#                 print(multi_(num1,num2))
#         elif operation == '/':
#                 print(div_(num1,num2))
#         else:
#             print('No such operation.')
#     else:
#         print('You should have entered "yes" or "no"!')



# def func_sum(*args):
#     return sum(args)

# print(func_sum(124,24,34,245,5,5,6))


# dct = {'name': 'Jamal', 'age': 16, 'city': 'Bishkek'}
# def keys(d):
#   for key in d.keys():
#     print(key)
# keys(dct)


# def types(a,b):
#     print(types(a, b)
#     return type(a), type(b)
# types('sdh', 345)



# def sum_(num):
#   res = 0
#   for i in str(num):
#     res += int(i)
#   return res
# print(sum_(3737664))

# num1 = int(input('Enter a number: '))
# def odd_even(num):
#   if num % 2 == 0:
#     print('It\'s even number.')
#   else:
#     print('It\'s odd number.')
# odd_even(num1)

# def check(s):
#     if s.lower()[::-1].split() == s.lower().split():
#         print('The word is a palindrome.')
#         return True
#     else:
#         print('The word is not a palindrome.')
#         return False
# print(check('Able was I ere I saw Elba'))


variable = 'makers'