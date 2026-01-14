# Користувач вводить із клавіатури числа. Програма повинна підраховувати суму, максимум і мінімум, введених чисел. Коли користувач вводить число 7 програма припиняє свою роботу і виводить на екран напис "Good bye!".

# min = None
# max = None
# sum = 0
# while True:
#     numb = int(input("Enter number "))
#     if numb == 7:
#         print("Good bye!")
#         break

#     sum += numb

#     if min == None:
#         min = max = numb
#         continue
    
#     if min > numb:
#         min = numb
#     if max < numb:
#         max = numb

# print(f"Sum :: {sum}")
# print(f"Min :: {min}")
# print(f"Max :: {max}")

# Напишіть програму, яка перевіряє, чи є введене користувачем число членом послідовності Фібоначчі.

# numb = int(input("Enter number "))
# a,b = 0,1

# # 13
# # a = 0, b = 1
# # a = 1, b = 1
# # a = 1, b = 2
# # a = 2, b = 3

# while a <= numb:
#     if a == numb:
#         print("True")
#         break
#     a,b = b, a + b
# else:
#     print("False")


# res = input('''
#         [1] - USA -> UAH
#         [2] - UAH -> USA
#         [0] - Exit
# ''')

# from datetime import datetime

# print(datetime.now().hour)
# print(datetime.now().minute)
# print(datetime.now().second)


# while True:
#     num = input()
#     if num == '0':
#         break

# print(datetime.now().hour)
# print(datetime.now().minute)
# print(datetime.now().second)
