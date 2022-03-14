# ЦИКЛЫ while, for

# while - endless cycle, it works while the condition is true
# counter = 0
# while counter < 500:
#     print(counter)
#     counter += 1
# Ctrl + C - to stop the cycle
# += increment
# -= decrement

# for - цикл по итерируемым обьектам
# for i in 'hello world':
#     print(i)

# ОПЕРАТОРЫ break & continue

# continue - пропуск текущей итерации
# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i*2)

# a = ['hello', 5, 'world', 'Python', 10]
# for i in a :
#     if i == 'Python':
#         continue
#     print(i)

# break - прерывает цикл
# db = []
# flag = True
# while flag:
#     data = input('Enter some data: ')
#     db.append(data)
#     answer = input('Continue? y or n: ')
#     if answer == 'n':
#         flag = False
# print(db)


# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i)
# else:
#     print('There is no such letter in the string') #doesn't interrupt the cycle


# lst = ['hello', 1, [True, False], 10]
# cnt = 0
# for i in lst:
#     cnt += 1
#     print(f'{cnt}. {i}!')


# for item_num, word in enumerate(lst):
#     print(f'{item_num + 1}. {word}!')

# print(list(enumerate(lst))) #returns list containing tuples

# CALCULATOR
while True:
    num1 = float(input('Please enter a number: '))
    sign = input('Please enter the action you need to calculate (+ or - or * or /): ')
    num2 = float(input('Please enter a number: '))
    if sign == '+':
        print(num1 + num2)
    elif sign == '-':
        print(num1 - num2)
    elif sign == '*':
        print(num1 * num2)
    elif sign == '/':
        print(num1 / num2)
    answer = input('Do you want to continue? (yes or no) ')
    if answer == 'no':
        break


# H/W - enвless calculation
