# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][2])

# matrix3D = [
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9],
#         [8,9,5]
#     ]
# ]
# print(matrix3D[0][1][2])
# for row in matrix:
#     for data in row:
#         print(data, end='\t')
#     print()

# for block in matrix3D:
#     for row in block:
#         for data in row:
#             print(data, end='\t')
#         print()
#     print()
# print(sum(matrix3D))

import random
# matrix = []

# for i in range(3):
#     row = []
#     for j in range(5):
#         row.append(random.randint(1,20))
#     matrix.append(row)


# matrix = [[random.randint(1,20) for i in range(5)] for j in range(3)]

# for row in matrix:
#     for data in row:
#         print(data, end='\t')
#     print()

# sum_ = 0
# for row in matrix:
#        sum_ += sum(row)
# for row in matrix:
#     for data in row:
#        sum += data
# print('Sum :: ', sum_)

# min_ = matrix[0][0]
# max_ = matrix[0][0]

# for row in matrix:
#      for data in row:
#           if min_ > data:
#                min_ = data
#           if max_ < data:
#                max_ = data

# for row in matrix:
#      if min_ > min(row):
#           min_ = min(row)
#      if max_ < max(row):
#           max_ = max(row)

# min_ = []
# max_ = []

# for row in matrix:
#      min_.append(min(row))
#      max_.append(max(row))

# min_ = min([min(row) for row in matrix])
# max_ = max([max(row) for row in matrix])
# print('Min :: ', min_)
# print('Max :: ', max_)

# min_ = matrix[0][0]
# max_ = matrix[0][0]
# min_col = 0
# min_row = 0
# max_col = 0
# max_row = 0
# for i in range(len(matrix)):
#      for j in range(len(matrix[i])):
#           if min_ > matrix[i][j]:
#                min_ = matrix[i][j]
#                min_row = i
#                min_col = j
#           if max_ < matrix[i][j]:
#                max_ = matrix[i][j]
#                max_row = i
#                max_col = j
# print(f'Max :: {max_} [{max_row},{max_col}]')
# print(f'Min :: {min_} [{min_row},{min_col}]')


# matrix = [[random.randint(1,20) for i in range(5)] for j in range(3)]

# clone = matrix.copy()
# print('Before copy')

# for i in range(len(matrix)):
#     print(id(matrix[i]), '\t', id(clone[i]))

# for i in range(len(clone)):
#     clone[i] = matrix[i].copy()

# print()

# for i in range(len(matrix)):
#     print(id(matrix[i]), '\t', id(clone[i]))

# print(f'Clone  :: {id(clone)}')
# print(f'Origin :: {id(matrix)}')
# clone[0][0] = 333
# print('Origin')
# for row in matrix:
#     for data in row:
#         print(data, end='\t')
#     print()
# print()

# print('Clone')
# for row in clone:
#     for data in row:
#         print(data, end='\t')
#     print()

row, col = 3,5
matr = [[random.randint(1,10) for i in range(col)] for j in range(row)]
total_sum = 0
for line in matr:
    sum_row = 0
    total_sum+=sum(line)
    for item in line:
        print(f'{item}', end='\t')
        sum_row+=item
    print(f'| {sum_row}')

print('-'*(col*9))

for i in range(col):
    sum_col = 0
    for j in range(row):
        sum_col+= matr[j][i]
    print(f'{sum_col}',end='\t')
print(f'| {total_sum}')