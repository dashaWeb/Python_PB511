
color = ['red','yellow','blue','orange']
print(type(color), id(color), color, sep='\n')

# str(), int(), float(), bool(), list()

print(color[1])
color[1] = 'black'
print(color)

for item in color:
    print(item)
    item = 'test'

print(color)

# for i in range(len(color)): # 0 1 2 3 4
#     color[i] = 'test'

# print(color)

# [start:stop:step]
print(color[2:])
print(color[::2])
print(color[::-1])

print('\n\n ============================ \n\n')

# Додати новий елемент до списку в кінець
print(f'\t Before :: {color}')
color.append('purple')
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')

# Додати новий елемент до списку за індексом
print(f'\t Before :: {color}')
color.insert(2,'brown')
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')



# Додати нові елементи до списку 
print(f'\t Before :: {color}')
color.extend(['gold','lime','green'])
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')

new_color = ['magenta','cyan','tomato']

print(f'\t Before :: {color}')
# color.append(new_color)
color.extend(new_color)
print(f'\t Before :: {color}')
print(f'\t After  :: {color[-1]}')

print('\n\n ============================ \n\n')
# Видалити елемент зі списку в кінці або за індексом
print(f'\t Before :: {color}')
color.pop()
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')

# 
print(f'\t Before :: {color}')
color.pop(4)
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')


# Видалити елемент зі списку за значенням
print(f'\t Before :: {color}')
if 'blue' in color:
    color.remove('blue')
else:
    print('Error')
print(f'\t After  :: {color}')

print('\n\n ============================ \n\n')

# очистити список
# color.clear()
# print(f'\t After  :: {color}')

# пошук індекса по значенню

print('Index:: ',color.index('lime'))
# print('Index:: ',color.index('hhhhh'))

for i in range(3):
    color.append('Red')


print(f'\t After  :: {color}')
print('\t Number of the word ', color.count('red'))
print('\n\n ============================ \n\n')

color.reverse()
print(color)

print('\n\n ============================ \n\n')

color.sort()
print(color)
print('\n\n ============================ \n\n')
color.sort(reverse=True)
print(color)
print('\n\n ============================ \n\n')


copy = color.copy()
print(f'{id(color)} \t Origin :: {color}')
print(f'{id(copy)}  \t Clone  :: {copy}')

print('\n\n ============================ \n\n')
copy[0] = 'violet'
print(f'{id(color)} \t Origin :: {color}')
print(f'{id(copy)}  \t Clone  :: {copy}')


import random
number = []

for i in range(10):
    number.append(i)
print(number)

number = [i+2 for i in range(10)]

print(number)

number = [random.randint(1,10) for i in range(10)]

print(number)
number.clear()

for i in range(1,4):
    for j in range(1,4):
        number.append(i*j)
print(number)

number = [str(i) + str(j) + str(q) if i != j != q != i else None for i in range(10) for j in range(10) for q in range(10)]

# 123

# for i in range(10):
#     for j in range(10):
#         for q in range(10):
#             print(str(i) + str(j) + str(q))

# print(len(number))
# number = set(number)
# print(number)
# number.remove(None)
# print(len(number))

# number = [1,2,3,4,1,2,5,3]
# print(number)
# print(set(number))


marks =[int(m) for m in input("Enter marks :: ").split() ]
# sum = 0
# for m in marks:
#     sum += int(m)

print(marks)
print('Sum :: ',sum(marks))
print('Min :: ',min(marks))
print('Max :: ',max(marks))
print('Avg :: ',sum(marks) / len(marks))
print(sorted(marks))
print(marks)
print(sorted(marks,reverse=True))

list_mark = '\n'.join('Mark ' + str(i) for i in marks)
print(list_mark)

