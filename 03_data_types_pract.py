
# number_1 = input("Enter first number :: ") #2
# number_2 = input("Enter second number :: ") #5
# number_1 = int(number_1)
# number_2 = int(number_2)

# # 2 + 5 = 7
# # print(number_1 , ' + ' , number_2 , ' = ' , number_1 + number_2 ,sep="\t")
# # print("{} + {} = {}".format(number_1,number_2, number_1 + number_2))
# print(f"{number_1} + {number_2} = {number_1 + number_2} \n{number_1} - {number_2} = {number_1 - number_2}")

# I                      I
#     LOVE        LOVE
#          Python

# print('''
#  I                      I
#      LOVE        LOVE
#           Python
# ''')

# Завдання 5
# Користувач із клавіатури вводить тризначне число. Наприклад, 891. Потрібно показати на різних рядках значення першого, другого і третього розряду. Також потрібно показати на окремому рядку суму цих трьох чисел. У нашому випадку це виглядатиме так:

# number = int(input("Enter number :: ")) #891

# # a = number // 100
# # print(a) #8
# # b = (number // 10) - a * 10 #9
# # print(b)
# # c = number - a * 100 - b * 10 # (891 - 800) = 91 -  90 = 1
# # print(c)

# c = number % 10 # 891 % 10 ->  1
# number = number // 10 # 891 // 10 --> 89

# b = number % 10 # 9
# number = number // 10 # 89 // 10 --> 8

# a = number % 10 # 8 % 10 --> 8
# number = number // 10 # 8 // 10

# print(a,b,c)

# Завдання 6
# Користувач вводить суму вкладу та відсоткову ставку. Напишіть програму, яка:
# Обчислює, скільки користувач отримає через 5 років, якщо щороку сума вкладу збільшується на вказаний відсоток.
# Виводить суму вкладу за кожен рік окремо.

sum = int(input("Enter money :: "))
percent = int(input("Enter percent :: "))

# res_perc = sum * 10 / 100
# sum = sum + res_perc
# sum = sum + 10
print(f"Start  :: {sum}")

sum += sum * 10 / 100 # sum = sum{1000} + (sum{1000} * 10 / 100){100} --> sum = sum{1000} + 100; sum{1100}
print(f"Year 1 :: {sum}")

sum += sum * 10 / 100 #sum = sum{1100} + (sum{1100} * 10 / 100){110} --> sum = sum{1100} + 110; sum{1210}
print(f"Year 2 :: {sum}")

sum += sum * 10 / 100 #sum = sum{1100} + (sum{1100} * 10 / 100){110} --> sum = sum{1100} + 110; sum{1210}
print(f"Year 3 :: {sum}")

sum += sum * 10 / 100 #sum = sum{1100} + (sum{1100} * 10 / 100){110} --> sum = sum{1100} + 110; sum{1210}
print(f"Year 4 :: {sum}")

sum += sum * 10 / 100 #sum = sum{1100} + (sum{1100} * 10 / 100){110} --> sum = sum{1100} + 110; sum{1210}
print(f"Year 5 :: {sum}")