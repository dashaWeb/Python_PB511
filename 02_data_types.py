# print("Hello World")
# print(123)

print(3, type(3))  # number (int)
print(3.2, type(3.2))  # number (float)
print(3.0, type(3.2))  # number (float)
print(.5, type(3.2))  # number (float)

print("Hello", type("Hello"))  # string (str)
print(True, type(True))  # boolean (bool)
print(False, type(False))  # boolean (bool)


# 2age = 18 error
age2 = 18
first_name = "Olena"
lastName = "Bondar"
first, second = 1, 2
flag = True

PI = 3.14

print("First name : ", first_name)
print(age2, " ---- ", type(age2))
print(first_name, " ---- ", type(first_name))
print(lastName, " ---- ", type(lastName))
print(first, " ---- ", type(first))
print(second, " ---- ", type(second))
print(flag, " ---- ", type(flag))
print(PI, " ---- ", type(PI))

# PI= 22
# print(PI, " ---- " , type(PI))


age2 = 17
print(age2, " ---- ", type(age2))

# Унарний оператор
# a = 2
# -a,

# Бінарний оператор
# a + b

# Тернарний оператор
# a ? b : c

# +,-,*,/,//,**,%

a, b = 15, 7
res_sum = a + b
print(a, "+", b, "=", res_sum)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)
print(a, "//", b, "=", a // b)
a = 2
b = 7
print(a, "**", b, "=", a ** b) # 2 * 2 * 2
print(a, "%", b, "=", a % b,)

result_info = first_name + " " + lastName
print(result_info) #"Olena Bondar"
print("Python" * 5)

# name = input("Enter name --> ")
# surname = input("Enter last name --> ")

# print("Result :: ", name, surname)

#task 1
# number_1 = input("Enter first number --> ") # "5"
# number_2 = input("Enter second number --> ") # "7"
# number_1 = int(number_1)
# number_2 = int(number_2)

# str()
# int()
# float()
# bool()
number_1 = float(input("Enter first number --> "))
number_2 = float(input("Enter second number --> "))

print("Result sum :: ", number_1 + number_2)

#  a + b * d - c / f
# 1. b * d
# 2. c / f
# 3. a + (b*d) 