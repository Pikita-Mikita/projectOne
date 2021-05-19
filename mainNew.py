# Примеры использования функций
def add(x, y):
    a = x + y
    print(a)
    return


def summa(a, b, c=4):
    return a + b + c


def sum1(*args):
    s = 0
    for i in args:
        s = s + i
    return s


def a(n):
    if n == 1:
        return 1
    else:
        return n - a(a(n - 1))


print(add(3, 6))
print(summa(4, 4, 5))
print(sum1(2, 4, 5, 6, 9))

for i in range(1, 10):
    print(a(i), end=" ")
