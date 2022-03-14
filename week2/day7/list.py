# lst = [] #empty list
# print(type(lst))

# lst = ['hello', 1, ['hello world', 5, []]]
# print(lst[2][1]) -> 5



# МЕТОДЫ СПИСКОВ:

# list.append(x) - добавление элемента в конец списка
# lst = ['Tom', 'Bob', 'Jack']
# lst.append('Jessica')
# print(lst)

# list.extend(list2) - расширение списка
# lst = ['Some data1', 'Some data2']
# lst2 = ['Some data3', 'Some data4']
# lst.extend(lst2) #берет данные из списка и расширяет первый список
# lst.append(lst2) #вкладывает второй список в первый
# print(lst)

# list.insert(i, x) -вставляет на i-ный элемент значение х (по индексу)
# lst = ['h', 'e', 'l', 'l', 'o']
# lst.insert(0, 'ne') 
# print(lst)

# list.remove(х) - удаляет первый элемент, имеющий значение х
# lst = ['h', 'e', 'l', 'l', 'o']
# lst.remove('h')
# print(lst)

# list.pop([i]) - удаляет i-ный элемент, если индекс не указан, то удалит последний и возвращает значение
# lst = ['h', 'e', 'l', 5, 2, 'l', 'o']
# removed_element = lst.pop(1)
# print(lst)
# print(removed_element) #возврат удаленного элемента

# list.index(x,[start],[end]) - возвращает положение первого заданного элемента(индекс)
# lst = ['h', 'e', 1, 8 , 'fhuhf', 'l', 'l', 'o']
# print(lst.index('e'))
# print(lst.index('l', 4, 8))

# list.count(x) - подсчет элементов со значением х
# lst = ['h', 'l','e', 1, 8 , 'fhuhf', 'l', 'l', 'o']
# print(lst.count('l'))

# list.sort() - сортировка, СНАЧАЛА НУЖНО ОТСОРТИРОВАТЬ
# lst = [5, 2, 4, 3, 1]
# lst2 = ['h', 'e', 'l', 'l', 'o']
# lst.sort()
# lst2.sort() #according to the alphabet
# print(lst)
# print(lst2)
# print(lst.sort()) #None

# list.reverse() - разворачивает список
# lst = [5, 2, 4, 3, 1]
# lst.sort()
# lst.reverse()
# print(lst)
# # OR
# print(lst[::-1]) 

# list.clear() - очищает список
# lst = [1, 5, 1, 1, 1, 'hello', [1, 2, 3]]
# lst.clear()
# print(lst)

# 'х'.join(list) - обьединение символов (с типом "строка") в строку, где х - обьединитель
# lst = ['w', 'o', 'r', 'l', 'd']
# result = ''.join(lst)
# print(result)




# КОПИРОВАНИЕ СПИСКОВ

# как делать нельзя (ссылаются на одну ячейку. При изменении одного листа, второй лист тоже будет меняться)
# lst1 = ['hello', 'world']
# lst2 = lst1
# lst1.append('HELLO')
# print(lst1)
# print(lst2)

# copy() - поверхностное копирование списков, копируя только верхний слой 
# lst1 = ['hello', 'world', [1,2,3]]
# lst2 = lst1.copy()
# # lst1.append('HELLO')
# lst1[-1].pop(0)
# print(lst1)
# print(lst2)

# deepcopy() - глубокое копирование всех слоев
# import copy
# lst1 = ['hello', 'world', [1,2,3, ['Tom', 'Jack']]]
# lst2 = copy.deepcopy(lst1)
# lst1[-1][-1].pop(0)
# print(lst1)
# print(lst2)


# INVITING TO A PARTY PEOPLE FROM THE LIST, EXCEPT FOR SAM
list_of_friends = ['Tom', 'John', 'Sam', 'Jessica', 'Helen']
for i in list_of_friends:
    if i != 'Sam':
        print(f'Welcome to party, {i}!')
