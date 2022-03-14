# МНОЖЕСТВА/СЕТ - НЕУПОРЯДОЧЕННЫЙ ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ {}, хранит уникальные значения и только неизменяемыe типы данных
# a = set()
# a = {'hello', 1, 2, 3}
# print(a)
# for i in a:
#     print(i)


# a = {'a', True, 125}
# print(len(a))
# print('a' in a)


# set1.isdisjoint(set2) - возвращает истину, если два сета не имеют общих элементов (True/False)
# a = {'hello', 1, 2}
# b = {'world', 5, 'John', 2}
# print(a.isdisjoint(b))


# СРАВНЕНИЕ
# a = {'hello', 1, 2}
# b = {'world', 5, 'John', 2}
# c = {'world', 5, 'John', 2}
# print(b == c)


# set1.issubset(set2)  OR  set1 <= set2 - все элементы одного сета принадлежат другому сету, является ли set1 подмножеством set2
# a = {'hello', 1, 2}
# b = {'hello', 1, 2, 'world'}
# print(a.issubset(b))
# print(a <= b)


# set1.issuperset(set2)  OR  set1 >= set2 - проверка на надмножество, является ли set1 надмножеством set2
# a = {'hello', 1, 2}
# b = {'hello', 1, 2, 'world'}
# print(b.issuperset(a))
# print(b >= a)


# set1.union(set2, [set3], ...)  OR  set1 | set2 | ...  - обьединение множеств
# b = {'world', 4, 'Tom', True}
# c = {'5', 7, 'Hello'}
# d = {15, 4, 'Helen'}
# print(b.union(c,d))
# print(b | c | d)


# set1.intersetion(set2, ...)  OR  set1 & set2 & ...  - пересечение множеств. Если нет общих элементов, возвращает пустой сет
# b = {'world', 4, 'Tom', True}
# c = {'5', 7, 'Hello'}
# d = {15, 4, 'Helen'}
# print(b.intersection(d))
# print(b & c & d)


# set1.difference(set2, ...)  OR set1 - set2 - ...  - разница множеств (что есть в set1, чего нет в set2)
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# d = {15, 4, 'Helen'}
# print(b.difference(c))
# print(b - c - d)


# set1.symmetric_difference(set2)  OR  set1 ^ set2  - все расходящиеся двух элементы  множеств
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# d = {15, 4, 'Helen'}
# print(b.symmetric_difference(c))
# print(b ^ c)


# True = 1
# False = 0
# Строка с пробелом = True
# Пустая строка = False


# set.copy() - копия множества
# import copy
# a = {'hello', 1, True}
# b = a.copy()
# c = copy.deepcopy(a)
# print(b)
# print(c)


# set1.update(set2, ...)  OR  set1 |= set2  - обьединение множеств, изменяя set1
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# d = {15, 4, 'Helen'}
# b.update(c, d)
# b |= c
# print(b)


# set1.intersection_update(set2, ...) OR  set1 &= set2  - апдейт set1 пересечением (общими элементами сетов), изменяет исходное множество set1
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# b.intersection_update(c)
# b &= c
# print(b)


# set1.difference_update(set2, ...)  OR  set1 -= set2  - апдейт разностью
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# b.difference_update(c)
# b -= c
# print(b)


# set1.symmetric_difference_update(set2)  OR set1 ^= set2  - апдейт все несхожие множества
# b = {'world', 5, 'Tom', True}
# c = {'5', 7, 'Hello', 5}
# b.symmetric_difference_update(c)
# b ^= c
# print(b)


# set1.update('Jack') - добавляет значение, разбивая посимвольно. НУЖНО ОБНОВЛЯТЬ СЕТ СЕТОМ


# set.add(element) - добавление элемента
# a = {'hello', 5, True, False}
# a.add('world')
# print(a)


# set.remove(element) - удаляет элемент из сета, returns False when element is missing
# a = {'hello', 5, True, False}
# a.remove(5)
# print(a)


# set.discard(element) - удаляет элемент, без возвращения ошибки
# a = {'hello', 5, True, False}
# a.discard(5)
# print(a)


# set.pop() - рандомно удаляет элемент из сета и возвращает удаленный элемент
# a = {'hello', 5, True, False}
# removed_element = a.pop()
# print(a)
# print(removed_element)


# set.clear() - очистка множества
# a = {'hello', 5, True, False}
# a.clear()
# print(a)


# frozen set - неупорядоченный, неизменяемый сет
# a = {'hello', 5, True, False}
# b = frozenset(a.copy())
# print(b)


# lst = [True, 5 , 'hello', 'hello', 15, False]
# lst = list(set(lst))  # удаление дубликатов, но порядок может изменится
# print(lst)




# TUPLES / КОРТЕЖ - УПОРЯДОЧЕННЫЙ, ИТЕРИРУЕМЫЙ, НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ. Но может хранить изменяемые типы данных, которые можно изменить
# tpl = tuple()
# tpl = ()
# print(tpl) #empty tuple


# tpl = (1, 'Hello', 1, [1, 5, 10])
# tpl[-1].append('World')
# print(tpl)
# print(tpl.count(1)) #подсчет количества заданного элемента в кортеже
# print(tpl.index('Hello')) #определение индекса элемента


# ЕСЛИ В tuple ХРАНИТСЯ ОДИН ЭЛЕМЕНТ, НУЖНО ПОСТАВИТЬ ЗАПЯТУЮ И ПРОБЕЛ ПОСЛЕ ЭЛЕМЕНТА
# tpl = (5,)
# var = 5
# print(tpl == var)
# print(type(tpl))


a = [set(), set(), set()]
inp1 = input()
inp2 = int(input())
for i in range(len(a)):
    if i == inp2:
        a[i].add(inp1)
    else:
        a[i].add('default value')
print(a)