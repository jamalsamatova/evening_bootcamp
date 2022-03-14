# range() - генератор последовательности

# for i in range(1, 11, 2):
#     print(i)


# list_ = range(1,11)
# list_ = list(range(1,11))
# list_ = tuple(range(1,11))
# print(list_)


# list_ = ['a', 'b', 'c', 'd']
# cnt = 0
# for i in list_:
#     print(f'{i} is under index {cnt}') # интерполяция - форматирование
#     cnt += 1


# list_ = ['a', 'b', 'c', 'd']
# for i in range(len(list_)):
#     print(f'{list_[i]} is under index {i}')
#     for j in 'hello':
#         print(j)


########################################################################
# LIST COMPREHENSION - представление списка
# list_ = []
# for i in range(0, 11):
#     list_.append(i)
# print(list_)


# list_ = [i for i in range(0,11)]
# list_ = [i**2 for i in range(0,11)]
# list_ = ['string' for i in range(0,11)]
# print(list_)


# list1 = [i for i in range(0,11) if i % 2 == 0]  # Если if без else, только после for
# list2 = [i if i % 2 == 0 else i**2 for i in range(0,11)]  # # Если if c else, только до for
# print(list1)
# print(list2)


# list_ = [i for i in range(0,11) for j in range(i)]
# print(list_)


########################################################################

# SET COMPREHENSION - генератор/представление множества
# set_ = {i for i in range(11)}
# print(set_)

########################################################################
# DICTIONARY COMPREHENSION
# dict_ = {i: i**2 if i % 2 == 0 else i ** 3 for i in range(11)}
# print(dict_)




import time
start = time.time()
list_ = []
for i in range(1000):
    list_.append(i)
end = time.time()
time1 = end - start


start = time.time()
list2 = [i for i in range(1000)]
end = time.time()
time2 = end - start

print(time1 / time2)


# list_ = [1,1,2,2,3,3,4]
# dct = {i: list_.count(i) for i in list_ }
# print(dct)


# list1 = list(range(1,11))
# list2 = ['yes' if j % 2 == 0 else 'no' for j in list1]
# print(list2)


# scores = {'Timur': {'history': 90, 'math': 95, 'literature': 91},'Olga': {'history': 92, 'math': 96, 'literature': 81},'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# subjects = {name: subject for name, dct in scores.items() for subject, score in dct.items() if score == max(dct.values())}
# print(subjects)



# import random
# set_ = f"В этом сете было {20 - len(set([random.randint(0, 100) for i in range(10)]).union(set([random.randint(0, 100) for i in range(10)])))} повторения, его длина составляет {len(set([random.randint(0, 100) for i in range(10)]).union(set([random.randint(0, 100) for i in range(10)])))}"
# print(set_)

  