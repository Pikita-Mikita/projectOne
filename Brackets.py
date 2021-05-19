# Программа проходится по тексту и удаляет все, что находится в скобках, а остальное оставляет как есть
f = open('in.txt')
n = open('out.txt', 'w')
firstLine = []
flag = 0

for line in f:
    for char in line:
        if flag == 0:
            firstLine.append(char)
            if char == '{':
                flag = 1
        elif char == '}':
            firstLine.append('}')
            flag = 0

A = "".join(firstLine)
print(A)

n.write(A)
n.close()
f.close()