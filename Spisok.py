# Работа с рандомным списком
from random import randint
a = [randint(-10, 10) for i in range(20)]
print("Рандомный список чисел:", a)
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
print("Список c нулями после макксимального элемента:", b)
print("Колличество нулей:", count_0)
print("Индекс максимального элемента:", maxEl)

