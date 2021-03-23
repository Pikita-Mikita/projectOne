names = ['Олег', 'Антон', 'Андрей']
for name in names:
    print("Имя игрока:", name)

n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print("Встретилось отрицательное число")
        break
else:
    print("Ни одного отрицательного числа")


a = int(input())
while a != 0:
    if a < 0:
        print("Встретилось отрицательное число")
        break
    a = int(input())
else:
    print("Ни одного отрицательного числа")







