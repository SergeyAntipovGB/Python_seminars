'''
Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
2 2
    4 
'''


def sum(a, b):
    if b == 0: return a
    a += 1          # допустимые по условию
    b -= 1          # арифметические действия
    return sum(a, b)

a = 5
b = 40
print(a, b)     # вывод на экран исходных чисел
if a < b: a, b = b, a   # расстановка чисел по возрастанию
print(sum(a, b))