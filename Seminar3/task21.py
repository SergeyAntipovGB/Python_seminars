import os
os.system('clear') 

'''
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''

l = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
startValues = list()
unicueValues = set()
for i in l:
    for value in i.values():
        startValues.append(value)
        unicueValues.add(value)
print(f'все значения словаря:\n{startValues}\n')
print(f'уникальные значения словаря:\n{unicueValues}\n')