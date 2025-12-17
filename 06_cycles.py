

'''
    while умова:
        тіло цикла 
'''

# i = 0 # лічильник
# while i < 5:
#     i+=1 # крок
#     print(f'{i}')

# number = int(input("Enter number --> "))  # 10
# i = 0
# while i <= number:
#     print(i, end='\t')
#     i += 1
# else:
#     print("\n finally")

# print("End program")


# sum = 0
# while True:
#     number = int(input("Enter number --> "))
#     if number == 0:
#         break
#     sum += number
# # else:
# #     print(f"Result :: {sum}") --> not work
# print(f"Result :: {sum}")

# 1 5 9 10 0
'''
sum += 1 {1}
sum += 5 {6}
sum += 9 {15}
sum += 10 {25}
'''

i = 0
while i < 5:
    i+=1
    color = input("Enter color : ")
    if color == 'red':
        continue
    
    print(i, color)
