# lst = [2,4,5,3,5,43,35,3]
# def lst_or_dct(list1):
#     choice = input('Choose list or dict: ')
#     if choice == 'list':
#         result = [i**2 for i in list1]
#     else:
#         result = {i: i**2 for i in lst}
#     return result
# print(lst_or_dct(lst))
    
######################################################################

# def hello():
#     print('Hello')

# def call():
#     while True:
#         answer = input('Do you want to stop (yes or no)? ')
#         if answer == 'yes':
#             break
#         hello()
# call()

################################################################

# def calculator():
#     num1 = float(input('Please enter a number: '))
#     sign = input('Please enter the action you need to calculate (+ or - or * or /): ')
#     num2 = float(input('Please enter a number: '))
#     if sign == '+':
#         print(num1 + num2)
#     elif sign == '-':
#         print(num1 - num2)
#     elif sign == '*':
#         print(num1 * num2)
#     elif sign == '/':
#         print(num1 / num2)

# def call(func):
#     while True:
#         answer = input('Do you want to stop (yes or no)? ')
#         if answer == 'yes':
#             break
#         func()
# call(calculator())

######################################################################

# import random
# def s_name():
#     name = input('Please enter your name: ')
#     surname = input('Please enter your surname: ')
#     password = generate_password(name, surname)
#     print(f'Your password is {password}.')  
# def generate_password(n, s):
#     password = n + s + ''.join([str(random.randint(0,10)) for i in range(7)])
#     return password 
# s_name()

#################################################################################

# readers = {}
# books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}

# def returned():
#     global books
#     global readers
#     name = input('Please enter your name: ')
#     conf = input(f'Do you want to return {readers[name]}? (yes or no) ')
#     if conf == 'yes':
#         returned_book = readers[name]
#         readers.pop(name)
#     books.update(returned_book)

# def get_info():
#     global books
#     print(books)

# def take():
#     global books
#     global readers
#     name = input('Please enter your name: ')
#     print(f'Choose on of the books: {books}')
#     book = input('Please enter the title: ')
#     taken = books.pop(book)
#     readers.update({name: {book:taken}})

# def library():
#     while True:
#         choice = input('Choose take, return or get (info). If you want to stop enter "stop"? ')
#         if choice == 'take':
#             take()
#         elif choice == 'return':
#             returned()
#         else:
#             get_info()
#         if choice == 'stop':
#             break

# library()

##################################################################

# Даны три числа x, y, z представляющие плоскости куба, также дано число n. Напишите функцию
# выдающую все возможные комбинации координат данных трех чисел, при условии что сумма x + y + z не должна равняться числу ограничению n. Для решения использовать list comprehensions. 
# Например: x, y, z = 1, 1, 2  ;  n = 4 
# правильный вывод: [[2, 1, 2], [1, 2, 2], [2, 2, 1]]
# xyz = list(map(int, input('Enter numbers: ').split()))
# n = int(input('Enter n: '))
# print(set([(x,y,z) for x in xyz for y in xyz for z in xyz if x + y + z != 4]))


