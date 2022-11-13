# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


n = int(input('---> '))

lst = ([randint(-n, n+1) for i in range(n)])
print(lst)

print([lst[i] for i in filter(lambda x: x % 2 != 1, range(n))])

print(sum([lst[i] for i in filter(lambda x: x % 2 != 1, range(n))]))

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв'
print(' '.join(list(filter(lambda x: 'абв' not in x, text.replace('абв', '').split()))))

