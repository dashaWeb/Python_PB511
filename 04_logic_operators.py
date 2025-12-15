# ==, !=, >, <, >=, <= (not)

# a = 5
# b = 7

# print(f"{a} == {b} --> {a==b}")  # False
# print(f"{a} != {b} --> {a!=b}")  # True
# print(f"{a} >  {b} --> {a>b}")  # False
# print(f"{a} <  {b} --> {a<b}")  # True
# print(f"{a} >= {b} --> {a>=b}")  # False
# print(f"{a} <= {b} --> {a<=b}")  # True

# # and - і
# # or - або

# login = "dev"
# password = "devuser"

# print(login == "mka" and password == "mka5")
# print((login == "mka" and password == "mka5") or (
#     login == "dev" and password == "devuser"))  # False
# color = "orange"
# print(color == "red" or color == "blue" or color == "green")
# print(f"a > b --> {'a' > 'b'}")
# print(f"a > b --> {'bC' > 'ba'}")
# print(int(True))
# print(int(False))

# print(5 + True)
# print(5 + False)

# year = int(input("Enter year --> "))

# print(365  + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))

# age = int(input("Enter your age --> "))
# if age >= 18 :
#     print("\033[32mWelcome\033[0m")
# else:
#     print("\033[31mError!! You are not yet of legal age to enter\033[0m")

# day = int(input("Enter number day --> "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error number")

# print("-------------")

# login = input("Хто прийшов --> ")
# if login.upper() == "Адмін".upper():
#     password = input("Пароль --> ")
#     if password == "ШАГ":
#         print("Ласкаво просимо")
#     elif password.lower() == "скасувати".lower():
#         print("Вхід скасований")
#     else:
#         print("Пароль невірний")
# # elif login == "Скасувати" or login == "скасувати":
# elif login.lower() == "Скасувати".lower():
#     print("Вхід скасований")
# else:
#     print("Я вас не знаю")


# number not[0,20]

number = int(input("Enter number --> "))
if number < 0 or number > 20:
    print("out in range")
elif number >= 0 and number <=20:
    print("in to the range")
