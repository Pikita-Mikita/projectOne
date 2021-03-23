import math

n = int(input('Длина последовательности'))  # Вводится длина последовтельности
x = float(input())  # Вводится переменная х
y = 1  # Искомая переменная y
step = 1  # Номер шага
while (step <= n):
    a = (-1) ** step * x ** step  # Числитель ряда
    b = math.factorial(step)  # Знаменатель ряда
    y += a / b  # Тут числитель разделить на знаменатель
    step += 1
print(y)

