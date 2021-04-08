def add(x, y):
    a = x + y
    print(a)
    return


add(3, 6)


def summa(a, b, c=4):
    return a + b + c


print(summa(4, 4, 5))


def sum1(*args):
    s = 0
    for i in args:
        s = s + i
    return s
X = 99
#global X  # Внутри функции показываем глобальную переменную, чтобы поменять ее

print(sum1(2, 4, 5, 6, 9))

#def a(n):
#    if n == 0:
#        return 1
#    else:
#       return a(n // 2) + a(n // 3)
#for  i in range(0, 10):
#    print(a(i), end=" ")


def a(n):
    if n == 1:
        return 1
    else:
        return n - a(a(n - 1))

for i in range(1, 10):
    print(a(i), end= " ")
