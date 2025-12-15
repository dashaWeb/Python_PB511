
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
# match day: # day == 
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Error")

'''
    31.03.2025 --> 01.04.2025
    28.02.2004 --> 29.02.2004
    28.02.2005 --> 01.03.2005
    31.12.2025 --> 01.01.2026
'''
day = int(input("Enter day :: "))
month = int(input("Enter month :: "))
year = int(input("Enter year :: "))

day_of_month = 0


print(f"{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}")
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        day_of_month = 31
    case 2:
        # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        #     day_of_month = 29
        # else:
        #     day_of_month = 28 
        day_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    case 4 | 6 | 9 | 11:
        day_of_month = 30

day+=1
if day > day_of_month:
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1

print(f"{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}")
# a ? b : c
# a if b else c