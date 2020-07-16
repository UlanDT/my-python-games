
import random
print("Введите 1 если 'Камень', 2 если 'Ножницы' или 3 если 'Бумага'")
n = random.randint(1,3)
# if n == 1:
#     print("Камень")
# elif n == 2:
#     print("Ножницы")
# else:
#     print("Бумага")
user_input = int(input("Enter: "))

if user_input == 1:
    if n == 1:
        print("Ничья")
    elif n == 2:
        print("Победа")
    else:
        print("Поражение")
elif user_input == 2:
    if n == 1:
        print("Поражение")
    elif n == 2:
        print("Ничья")
    elif n == 3:
        print("Победа")
else:
    if n == 1:
        print("Победа")
    elif n == 2:
        print("Поражение")
    else:
        print("Ничья")
