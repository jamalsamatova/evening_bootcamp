# def func1():
#     return 'smth'

# def func2(func):
#     print('Before func calling')
#     print(func())

# func2()

##############################################################################

# def func_dec(function_to_decorate):
#     def wrapper(): #принято называть враппер
#         print('Код, который отрабатывает до вызова функции.')
#         function_to_decorate()
#         print('Код, который отрабатывает после вызова функции.')
#     return wrapper

# @func_dec
# def func1():
#     print('Просто функция :)')

# func1()

##############################################################################

# def bread(func):
#     def wrapper():
#         print('/ bread \\')
#         func()
#         print('\ bread /')
#     return wrapper

# def ingridients(func):
#     def wrapper():
#         print('-tomato-')
#         func()
#         print('-salad-')
#     return wrapper

# @bread
# @ingridients
# def get_sandwich(meat = '---meat---'):
#     print(meat)

# get_sandwich()

##############################################################################

# def benchmark(func):
#     import time

#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'func execution is {end-start}')
#     return wrapper

# @benchmark
# def call_webpage():
#     import requests
#     webpage = requests.get('https://google.com')

# call_webpage()

# @benchmark
# def iterate_list():
#     for i in range(1, 50):
#         print(i**2 - 20)

# iterate_list()

##############################################################################

# def decorator(func):
#     def wrapper(arg1):
#         print(f'{arg1}')
#         func(arg1)
#     return wrapper

# @decorator
# def func(word):
#     print(f'the word is {word}')

# func('yes')

##############################################################################

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'see args {args}')
#         print(f'see kwargs {kwargs}')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func_without_params():
#     print('func without params')

# @decorator
# def func_with_params(first_name, last_name):
#     print('func with params')
#     print(f'hello, {first_name} {last_name}')

# @decorator
# def func_with_params_kwargs(first_name, last_name):
#     print('func with params kwargs')
#     print(f'Hello, {last_name} {first_name}')


# func_without_params()
# func_with_params('Jamal', 'Samatova')
# func_with_params_kwargs(first_name = 'Jamal', last_name = 'Samatova')

##############################################################################

def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0 
            for i in range(iters):
                start = time.time()
                func_call = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'Average time: {total/iters}')
            return func_call
        return wrapper
    return actual_decorator

@benchmark(iters=20)
def get_webpage(url):
    import requests
    webpage = requests.get(url)

get_webpage('https://yandex.ru')



