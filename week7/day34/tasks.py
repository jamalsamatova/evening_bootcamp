# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance

#     def fill(self, amount):
#         self.balance += amount
#         return self.balance

#     def check(self):
#         return self.balance

# a = BankAccount(5000)
# a.withdraw(2000)
# a.fill(1000)
# print(a.check())

####################################################################
from functools import reduce

class Task:
    def __init__(self, task, priority = 3):
        self.task = task
        self.priority = priority

    def __str__(self):
        return f'I have {self.task} to do, it\'s priority level is {self.priority}'

class ToDoList:
    tasks = {}
    def __init__(self):
        self.tasks = []
    
    def put(self, todo):
        self.tasks.append(todo)

    def get(self):
        if not (get := [[i.task, i.priority] for i in self.tasks]):
            return None
        max_value = list(reduce(lambda x, y: x if y[1] < x[1] else y, get))
        return f'My highest priority is to {max_value[0]}'

    def count(self, pr = 1):
        self.pr = pr
        self.counts = []
        for i in self.tasks:
            if self.pr in range(1,6):
                if i.priority == self.pr:
                    self.counts.append(i)
                    print(i)
            else:
                self.pr = 0
        return f'I have {len(self.counts)} tasks with priority level of {self.pr}'         

todolist = ToDoList()
task1 = Task('buy milk')
task2 = Task('visit my parents', 4)
task3 = Task('refactor my code', 5)
task4 = Task('apply for a new job', 5)

todolist.put(task1)
todolist.put(task2)
todolist.put(task3)
todolist.put(task4)

print(todolist.get())

