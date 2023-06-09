'''
Задача No45. Решение в группах
Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n) равна
числу m и наоборот. Например, 220 и 284 – дружественные числа. По
данному числу k выведите все пары дружественных чисел, каждое из
которых не превосходит k. Программа получает на вход одно натуральное
число k, не превосходящее 105. Программа должна вывести все пары
дружественных чисел, каждое из которых не превосходит k. Пары
необходимо выводить по одной в строке, разделяя пробелами. Каждая
пара должна быть выведена только один раз (перестановка чисел
новую пару не дает).
Ввод: Вывод:
300 220 284
10 минут
'''


def div(max, count = 0, step = 1):
    '''
    Функция возвращает count - количество
    делителей заданного числа max: [1, max)
    '''
    if step == max // 2 + 1: return count
    if max % step == 0: count += step
    return div(max, count, step + 1)

def sum(step1, step2):
    '''
    Функция выбирает пары дружественных чисел
    из заданного промежутка [1, k]
    '''
    if step1 == 1: return
    if step2 == 0: sum(step1 - 1, step1 - 2)
    else:
        if div(step1) == div(step2): print(step1, step2)
        sum(step1, step2 - 1)    
        
k = 16
sum(k, k - 1)

# def sum(friends):     # вариант решения вложенными циклами
#     for i in range(k, 1, -1):
#         first = div(i)
#         for j in range(i - 1, 0, -1):
#             second = div(j)
#             if first == second:
#                 print(i, j)
#                 break