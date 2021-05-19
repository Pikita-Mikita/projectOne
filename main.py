import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = []

# Создаем рандомную матрицу с заданным числом строк и столбцов
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(random.randint(-5, 5))

# Выводим матрицу в консоль
for i in range(n):
    print("")
    for j in range(m):
        print(matrix[i][j], end=' ')

# Ищем количество положительных, отрицательных чисел и нулей
count_positive = 0
count_negative = 0
count_zero = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > 0:
            count_positive += 1
        elif matrix[i][j] < 0:
            count_negative += 1
        else:
            count_zero += 1
print("")
print("Количество положительных чисел:", count_positive)
print("Количсетво отрицательных чисел:", count_negative)
print("Количсетво нулей:", count_zero)

