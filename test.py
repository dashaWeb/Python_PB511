import random
print("Завдання 4")

matrix = [[random.randint(1, 20) for i in range (5)] for j in range(5)]

print("Матриця: ")
for row in matrix:
    for data in row:
        print(data, end='\t')
    print()

row_sum = []
for i in range(5):
    sum = 0
    for j in range(5):
        sum += matrix[i][j]
    row_sum.append(sum)
    print("Сума рядків --> ", sum)
    
# data_sum = []
# for i in range(5):
#     sum = 0
#     for j in range(5):
#         sum += matrix[i][j]
#     data_sum.append(sum)
#     print("Сума рядків --> ", sum)

total = 0
for i in range(5):
    for j in range(5):
        total += matrix[i][j]
print("Загальна сума: ", total)