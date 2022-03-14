# import os
# Работа с текстовым форматом файла
# # open(path, method / regime) 
# f = open('test.txt', 'r')
# print(f'1. {f.read()}') # курсор ушел до конца
# f.seek(0) # задаем с какого символа начать чтение, переносим курсор на нужно положение
# print(f.read(10)) # вытаскивает текст по количеству символов
# print(f.read(10))

# f = open('test.txt', 'rt')
# print(f)
# for line in f: # иклом перебрали и распечатали строки
#     print(line)

###############################################################

# r|t - чтение текста
# r(read) - чтение данных
# w(write) - открывает файл для записи (создает новый файл или очищает содержимое файла, если файл существует)
# x(exclusive) - открывает для записи, только если его не существует => создает файл
# a(append) - открывает файл для записи, добавляет последний элемент

###############################################################

# f.write() - перезапись
# f = open('test.txt', 'wt')
# f.write('Hello world!') 
# f.write('Lalalala')
# f.close()

# try:
#     f = open()
#     f.write()
# finally:
#     f.close()

###############################################################

# f = open('test.txt', 'r')
# file_content = f.read()
# print(file_content)
# print('---------------')
# print(f.tell()) # на какой позиции курсор
# f.seek(10)
# print(f.read())
# f.close()

###############################################################

# f = open('test.txt', 'r')
# print(f.readline()) # чтение файла построчно
# print(f.readline())

###############################################################

# f = open('test.txt', 'r')
# content = f.readlines()
# # print(content)
# for item in content:
#     print(item)

###############################################################

# f = open('test.txt', 'w+')
# f.write('string1\n')
# f.write('string2')
# f.close()
# f .writelines(['Hello\n', 'world!\n'])
# f.seek(0)
# print(f.read())
# f.close()

# f = open('test.txt', 'a+')
# f.writelines(['hello world\n', 'harry potter\n']) # добавление строчек
# f.close



# JSON = JavaScript Object Notation
# Frontend(form) -> JSON -> Backend -> parse JSON -> python data
# file.json

# [{"name": 'Tom', 'age': 37, 'country': 'KG'}, {"name": 'Tom', 'age': 37, 'country': 'KG'}, {"name": 'Tom', 'age': 37, 'country': 'KG'}]

# import json
# data = {"name": 'Tom', 'age': 37, 'country': 'KG'}
# print(type(data))
# json_obj = json.dumps(data) # данные переводятся в json
# print(json_obj)
# print(type(json_obj))

# python_obj = json.loads(json_obj) # данные из json переводятся в python
# print(python_obj)
# print(type(python_obj))


# Python -> JSON
# dict -> Object
# list -> Array
# tuple -> Array
# str -> String
# int -> Number
# float -> Number
# True -> true
# False -> false
# None -> null



# Работа с файлами JSON
# import json
# data = {"name": 'Tom', 'age': 37, 'country': 'KG'}
# with open('data.json', 'a+') as f:
#     json.dump(data, f) #


# import json
# with open('data.json', 'r+') as f:
    # python_obj = json.loads(f.read())
    # python_obj = json.load(f)
    # print(type(python_obj))



# def write_to_txt():
#     data = input('Enter some data: ') + '\n'
#     with open('user_data.txt', 'a+') as file_:
#         file_.writelines(data)

# def manager():
#     while True:
#         write_to_txt()
#         answ = input('Write more? (yes or no) ') 
#         if answ == 'no':
#             break
# manager()



with open('google_kazakstan.txt', 'a+') as kz, open('google_paris.txt', 'a+') as par, open('google_poland.txt', 'a+') as pl, open('google_kyrgyzstan.txt', 'a+') as kg, open('google_san_francisco.txt', 'a+') as sf, open('google_germany.txt', 'a+') as de, open('google_moscow.txt', 'a+') as msc, open('google_sweden.txt', 'a+') as se:
  while True:
    offices = [kz, par, pl, kg, sf, de, msc, se]
    print('[kz, par, pl, kg, sf, de, msc, se].')
    office = int(input('Enter the index of the office. ')) - 1
    data = input('Enter some data (to finsih enter "stop"): ') 
    offices[office].write(data + '\n')
    if data == 'Hello':
      complaint = input('Enter your complaint: ')
      offices[office].write('Complaint: ' + complaint)
    elif data == 'stop':
        break

