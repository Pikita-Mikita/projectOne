w = int(input("Ввести время суток от 0 до 24: "))
if w > 24:
    print("Ввели число больше 24")
elif 12 > w >= 6:
    print("Утро")
elif 18 > w >= 12:
    print("Обед")
elif 24 >= w >= 18:
    print("Вечер")
elif 6 > w >= 0:
    print("Ночь")