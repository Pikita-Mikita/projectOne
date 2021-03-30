import random
a = [random.randint(-10, 10) for i in range(10)]  # Создаем рандомный список
print("Рандомный список элементов:", a)
minElement = 300

negative  = 0
for i in range(len(a)):
    if a[i] < minElement:
        minElement = a[i]
min_index = a.index(minElement)
print("Значение минимального элемента:", minElement)
print("Индекс минимального элемента:", min_index)
l = len(a)
for i in range(l):
    if a[i] < 0 and i > min_index:
       a[i] = 'X'
       negative += 1
for i in range(negative):
    a.remove('X')
print("Список без отрицательных элементов:", a)
