# lst = [1, 2, 3, 4, 5]
# lst1 = []
# for i in lst:
#     if type(i) == int:
#         i = str(i)
#     lst1.append(i)
# print(lst1)


# data_base = []
# while True:
#     q = input('Write(w) or delete(d)? ')
#     if q == 'w':
#         data = input('Enter some data: ')
#         data_base.append(data)
#         print(f'You have successfuly entered your data! {data_base}')      
#     else: 
#         index = int(input('Please enter the index of the data you want to delete: '))
#         data_base.pop(index-1)
#         print(f'You have successfuly deleted the data! {data_base}')
#     c = input('Continue (yes or no)? ')
#     if c == 'n':
#         break


# list_of_names = [('Jack', 25), ('Helen', 18), ('Mike', 15), ('Jessica', 32), ('Jack', 25), ('Alice', 28), ('Mike', 15)]
# new_list = list(set(list_of_names))
# for i in new_list:
#     if i[1] >= 18:
#       print(f'Hello, {i[0]}! We are pleased to inform you that our store has a huge disount on alcohol!' )

"""
4 таск
в новый год вы решили сделать друзьям подарки, список друзей выглядит след.
образом: ['Tom', 'Jessica', 'Helen', 'Jim', 'Bob', 'Alice'], у вас есть определенное количество подарков
различных категорий, представлено в след виде: [['Harry Potter', 'It', 'Rich&Poor Dad'],
['Samsung Phone', 'Xiaomi Phone', 'iPhone'], ['20% Gucci discount', '10% LV discount', '15% Apple discount']],
использую встроенный модуль рандом, необходимо каждому другу выбрать подарок и результат
в следующем виде вывести в терминал:
'Tom' --> 'Xiaomi Phone'
'Jessica' --> '20% Gucci discount'
'Helen' --> 'Rich&Poor Dad'
и тд.
для каждого друга рандомно должна выбираться категория подарков и рандомный подарок из этой категории соответственно.
Требования: использовать рандом, каждому другу должен достаться уникальный
подарок(т.е. нельзя дарить один подарок нескольким)
"""
# import random
# list_of_friends = ['Tom', 'Jessica', 'Helen', 'Jim', 'Bob', 'Alice']
# presents = [['Harry Potter', 'It', 'Rich&Poor Dad'],
# ['Samsung Phone', 'Xiaomi Phone', 'iPhone'], ['20% Gucci discount', '10% LV discount', '15% Apple discount']]

# list_of_presents = []
# for i in list_of_friends:
#     category = random.choice(presents)
#     if category == []:
#         category = random.choice(presents)
#     present = random.choice(category)
#     category.remove(present)
#     print(f'{i} --> {present}')


name_of_list = ['Helloworld!']
word = name_of_list[0]
length = len(word)//2 + len(word)%2
new_word = word[length:] + word[0:length]
print(list(new_word))