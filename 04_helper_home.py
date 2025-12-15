# Користувач вводить тризначне число. Програма повинна визначити, чи всі цифри числа однакові. Якщо всі цифри
# однакові, вивести «Всі цифри однакові», інакше — «Цифри різні».

number = int(input("Enter number :: ")) #456

if number > 99 and number < 1000:
    c = number % 10
    number //= 10 # number = number // 10
    b = number % 10
    number //= 10 # number = number // 10
    a = number % 10
    number //= 10 # number = number // 10
    if c == b and b == a:
        print("«Всі цифри однакові»")
    else:
        print("«Цифри різні»")
else:
    print("Error")


