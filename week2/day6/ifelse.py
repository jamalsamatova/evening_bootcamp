# a = True
# b = False 
# print(type(a))

# if 
# if else 
# if elif else


# and -> и 
# True and True == True
# True and False == False 
# False and False == False


# or -> или
# True or False == True
# True or True == True
# False or False == False


# not -> нет
# not False == True
# not True == False
# not (True or False) == False
# not (False or False) == True
# not (True or True) == False


# !=  --> НЕ РАВНО
# 1 == 1 -> True
# 1 == 0 -> False
# 1 != 1


# == -> ОПЕРАТОР СРАВНЕНИЯ
# a = 1
# b = 0
# a == b -> False
# a != b -> True
# c = a == b
# print(c) -> False


# if condition:
#     statement 1
#     statement 2


# x = int(input('Enter a number: '))
# y = int(input('Enter a number: '))
# if x > 0 and y > 0:
#     print('All numbers are greater than 0')


# x = 1
# y = 5
# if not (x == True and y != 5):
#     print(True)


# number = int(input('Enter a number: '))
# if number > 5:
#     print('Your number is greater than 5')


# four = '4'
# if len(four) != 4:
#     print(True)


# a = 4
# if a == 2 + 2:
#     print(a)


# МОРЖОВЫЙ ОПЕРАТОР
# a = 5
# print(b := a + 5)

# IFELSE
# if condition:
#     statement 1
#     statement 2
#     ...
# else:
#     statement 1
#     statement 2
#     ...


# a = True
# b = False

# if a:
#     print(True)
# else:
#     print(False)

# if not a:
#     print('The condition is true')
# else:
#     print('The condition is false')


# number = int(input('Enter a number: '))
# if number > 10:
#     print('Your number is grater than 10.')
# else:
#     print('Your number is not grater than 10.')


# password = input('Enter your password: ')
# if password == 'qwerty123':
#     print('Welcome user!')
# else:
#     print('Wrong Password')


# bank_account = 3000
# withdraw = float(input('Enter sum: '))
# if bank_account > 0:
#     if withdraw < bank_account:
#         print(f'your balance is {bank_account - withdraw} soms')
#     else:
#         print('not enough money')
# else:
#     print('Fill your balance')


# username = input('Enter your username: ')
# if username == 'admin':
#     password = input('enter password: ')
#     if password == 'admin123':
#         print('welcome user')
#     else: 
#         print('incorrest password')
# else:
#     print('username not found')


# score = int(input('Enter your mark: '))
# if score >= 90:
#     print('5')
# else:
#     if score >= 80:
#         print('4')
#     else:
#         if score >= 70:
#             print('3')
#         else:
#             if score >= 60:
#                 print('2')
#             else:
#                 print('Your didn\'t pass')

# ELIF 
# if condition1:
#     statement1
#     statement2
#     ...
# elif condition2:
#     statement1
#     statement2
#     ...
# elif condition3:
#     statement1
#     statement2
#     ...
# ...
# else:
#     statement1
#     statement2 
#     ...


# score = int(input('enter your mark: '))
# if score >= 90:
#     print('5')
# elif score >= 80:
#     print('4')
# elif score >= 70:
#     print('3')
# elif score >= 60:
#     print('2')
# else:
#     print('You didn\'t pass the exam')


# number = int(input('Please enter a number: '))
# if number % 5 == 0 and number % 3 ==0 :
#     print('HahaHoo')
# elif number % 3 == 0:
#     print('Haha')
# elif number % 5 == 0:
#     print('Hoo')
# else:
#     print('Aaaaa')


# count = 0
# number = input('Please enter an integer number: ')
# if number.isdigit():
#   count = int(number)
# print(count)


# num = int(input('Please enter an integer number: '))
# if num >= 65 and num <= 90 or num >= 90 and num <= 122:
#   print(f'Это буква, "{chr(num)}"')
# else:
#   print(f'Это не буква, это символ "{chr(num)}"')


num = int(input('Please enter a number: '))
user_choice = input('Please select and write down what you want to convert: "KB to Byte" or "Byte to KB": ')
if user_choice == 'KB to Byte':
  print(num * 1024)
elif user_choice == 'Byte to KB':
  print(num / 1024 )


