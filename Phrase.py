# Работа со строками
phrase = input("Введите любую фразу длинной от 10 символов: ")
if len(phrase) > 10:
    print("Первые 4 символа: " + phrase[:4])
    print("Пocледние 4 символа: " + phrase[-4:])
    print("Символы с 3 по 8: " + phrase[2:8])
else:
    print("Вы ввели фразу меньше 10 символов.")