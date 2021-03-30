'''import random
a = random.randint(1, 10)  # Генерирует рандомные целые числа от 1 до 10
print(a)

maxChislo = 0
for i in range(20):
    if i > maxChislo:
        maxChislo = i

print(list('Список'))
s = ['t', 2]
print(s)

f = 'Привет'
c = [c + d for c in f for d in f]
print(c)

from random import randint
A = [randint(-10, 10) for i in range(20)]
print(A)

B = []
for i in B:
    B.append(range(1, 20))

print(B)  '''

from random import randint
a = [randint(-10, 10) for i in range(20)]
print(a)
b = []
x = len(a)
maxEl = 0  # Индекс максимального элемента
count_0 = 0  # Количество нулей
for i in range(len(a)):  # Проходится по всем индексам списка а
    if a[maxEl] < a[i]:  # Сравнивает значения следующего элемента с предыдущим
        maxEl = i  # Присваивает индекс большего элемента в переменную maxEl
    if a[i] == 0:
        count_0 += + 1  # Считает нули

for i in range(len(a)):
    if i < maxEl + 1:
        b.append(a[i])
for j in range(count_0):
    b.append(0)
print(b)
print(count_0)
print(maxEl)

''' list.insert(i, x)   # Пригодится для решения

maxEl = 0   # Индекс максимального элемента
for i in range(len(A)): # Выдаст все  индексы
    if A [maxEl] < A[i]:
        maxEl = i
# В цикле  for пойти по элементам списка list.remove(использовать эту команду)
# Подсччитать количество  нулей
# if A[i] = 0 завели счетчик
# Сгенерируем новый список, вместо того, чтобы вставлять в этот же
# Копировать с  помощью аппенда, сначала все остальные числа, потом максимальное и нули, и остальные числа
# Сначлаа найти максимальны элемент, его индекс и кол-во нулей, потом начать копирование в другой список
# for j in range(переменная с  количеством нулей)
# B.append(0)#
'''