# Программа обрабатывает графы

def read_graph():
    m = int(input('Введите кол_во вершин:'))
    n = int(input('Введите кол_во ребер:'))
    matrix = []
    for i in range(m):  # создаем матрицу с наполнением 0
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
            print(matrix[i][j], end=' ')  # не обязательно принтовать
        print(' ')
    count_loop = 0
    for i in range(n):  # заполняем матрицу связями ребер
        a, b = input('').split()
        a = int(a)
        b = int(b)
        add_edge(matrix, a, b)
        add_edge(matrix, b, a)
        if a == b:  # Проверяем есть ли в графе петли
            count_loop += 1
    print("Количество петлей в графе:", count_loop)

    return matrix


def add_edge(g, a, b):
    g[a][b] = 1


g = read_graph()  # распечатать в виде матрицы
for i in range(len(g)):
    print('')
    for j in range(len(g)):
        print(g[i][j], end=" ")

print('')

for i in range(len(g)):  # Печатаем для каждой вершины номера смежных вершин

    for j in range(len(g)):
        if g[i][j] == 1:
            print("Смежная вершина для", i, ",будет", j)

print(' ')

countZeros = 0
countTops = []
for i in range(len(g)):  # Ищем номера вершин со всеми нулями
    for j in range(len(g)):
        if g[i][j] == 0:
            countZeros += 1
    if countZeros == len(g):
        countTops.append(i)
        countZeros = 0
    else:
        countZeros = 0
print("Номера вершин со всеми нулями:", countTops)

countOnes = 0
countTopsForOnes = []
for i in range(len(g)):  # Ищем вершины со всеми единицами
    for j in range(len(g)):
        if g[i][j] == 1:
            countOnes += 1
    if countOnes == len(g):
        countTopsForOnes.append(i)
        countOnes = 0
    else:
        countOnes = 0
print("Номера вершин со всеми единицами:", countTopsForOnes)

print(' ')

countOnes = 0
countTopsForOnes = []
n = 0  # Переменная для нахождения максимальной вершины
for i in range(len(g)):  # Ищем степень для каждой вершины
    for j in range(len(g)):
        if g[i][j] == 1:
            countOnes += 1
    print("Степень для вершины", i, "будет:", countOnes)
    if countOnes > n:  # Находим максимальную вершину
        n = countOnes
    if countOnes == 1:
        print("Вершина со степенью 1:", i)
    else:
        pass
    countOnes = 0
print(' ')
print("Максимальная степень вершин:", n)



