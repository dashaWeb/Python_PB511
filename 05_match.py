
# day = int(input("Enter number (1 - 7)"))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Wednesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error")
# match day: # day == case 1
#     case 1:
#         print("Monday")
#     case 2: day == case 2
#         print("Tuesday")
#     case 3: day == case 3
#         print("Wednesday")
#     case _:
#         print("Error")

# '''
#     31.03.2025 --> 01.04.2025
#     28.02.2004 --> 29.02.2004
#     28.02.2005 --> 01.03.2005
#     31.12.2025 --> 01.01.2026
# '''
# day = int(input("Enter day :: "))
# month = int(input("Enter month :: "))
# year = int(input("Enter year :: "))

# day_of_month = 0


# print(f"{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}")
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         day_of_month = 31
#     case 2:
#         # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         #     day_of_month = 29
#         # else:
#         #     day_of_month = 28 
#         day_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#     case 4 | 6 | 9 | 11:
#         day_of_month = 30

# day+=1
# if day > day_of_month:
#     day = 1
#     month += 1
# if month > 12:
#     month = 1
#     year += 1

# print(f"{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}")
# # a ? b : c
# # a if b else c

# percent = 0.0
# age = 18
# if age < 18:
#     percent = 0.10
# elif age >= 18 and age <= 60:
#     percent = 0.05
# else:
#     percent = 0.15

# sum = 1000
# sum = sum - (sum * percent)

# 100
# .20
# 1.50

# percent = 20

#  20 / 100 --> 0.2
# 150 / 100 --> 1.5

# Користувач вводить оцінки з чотирьох предметів (від 1 до 5). Програма перевіряє, чи може він бути допущений до іспиту:
# Якщо хоча б одна оцінка нижче 3, студент не допускається до іспиту.
# Якщо всі оцінки 4 і вище, студент допускається до іспиту з відзнакою.
# У всіх інших випадках студент допускається до іспиту.

# rat_1 = int(input("Enter mark --> "))
# rat_2 = int(input("Enter mark --> "))
# rat_3 = int(input("Enter mark --> "))
# rat_4 = int(input("Enter mark --> "))

# if rat_1 < 1 and rat_1 > 5 or rat_2 < 1 and rat_2 > 5 or rat_3< 1 and rat_3 > 5 or rat_4 < 1 and rat_4 > 5 :
#     print("Invalid value mark")
# else:
#     if rat_1 < 3 or rat_2 < 3 or rat_3 < 3 or rat_4 < 3:
#         print('студент не допускається до іспиту')
#     elif rat_1 >= 4 and rat_2 >= 4 and rat_3 >= 4 and rat_4 >= 4:
#         print('студент допускається до іспиту з відзнакою')
#     else:
#         print('студент допускається до іспиту')

# letter = 'a'
# code = 97
# # print(chr(97))
# # print(chr(9786))
# # print(ord('a'))

# if letter == 97:
#     print('a')

# match letter:
#     case 97:
#         print('a')
#     case 98:
#         print('b')
#     case 99:
#         print('c')
