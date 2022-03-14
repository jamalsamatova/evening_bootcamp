# def info(name, age, work):
#     print(f'Hello, {name}, {age}, {work}.')

# info() --> TypeError
# info('IT', 'Tom', 30) #именованные
# info(work = 'IT', name = 'Tom', age =  30) #позиционные

# positional argument follows keyword argument --> SyntaxError

# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)
# test('Hello', 123, name = 'Tom', work = 'IT')



# def hello_func(age, name = 'Guest'): #default argument
#     return f'Hello, {name}, you are {age} y.o.'
# print(hello_func(30, 'Tom'))


# db = {'hello': 123, 'hello2': 456}
# print(db['hello23'])
# print(db.get('hello23')) #returns None if no such key


# string = input('Enter a string: ').lower()
# def translate_str(string):
#     intab = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#     outtab = "йцукенгшщзхъфывапролджэячсмитьбю"
#     transtab = str.maketrans(intab, outtab)
#     return string.translate(transtab)
# result = translate_str(string)
# print(result)


# task
# import datetime
# hour_time = datetime.datetime.now().hour
# db = {'Tom': '+999777888', 'Helen': '+888777222', 'Bob': '+777555333'}
# def do_obeda(name, phone):
#     print(f'Discount on coffee for {name} with phone number: {phone}.')
# def posle_obeda(name, phone):
#     print(f'Discount on  for {name} with phone number: {phone}.')
# for name, phone in db.items():
#     if hour_time < 13:
#         do_obeda(name,phone)
#     else:
#         posle_obeda(name,phone)


# c = {'RUB': 1.24, 'USD': 84.7, 'EUR': 94.8}

# def trans(amount, currency):
#     for k,v in c.items():
#         if currency == k:
#             result = round(amount / v, 2)
#     return result
# amount = int(input('Enter money: '))
# currency = input('Choose currency: ')
# print(trans(amount, currency))

# import random
# tries = 1
# comp = random.randint(1,11)

# while tries <= 3:
#     guess = int(input('Enter your number: '))
#     tries += 1

variable = 'makers'


