numb = input("Введите трехзначное число:")
while len(numb) > 3:
    numb = input("Введите трехзначное число:")
else:
    if numb[0] == numb[1] == numb[2]:
        print("Все цифры в числе равны")
    else:
        print("Цифры в числе не равны")


