

# for j in range(2,10):
#     for i in range(1,11):
#         print(f'{i} x {j} = {i * j}')


# for i in range(1,11):
#     print(f'{i} x {3} = {i * 3}')


# for i in range(1,11):
#     print(f'{i} x {4} = {i * 4}')

# print(f'1 x {numb} = {1 * numb}')
# print(f'2 x {numb} = {2 * numb}')
# print(f'3 x {numb} = {4 * numb}')
# print(f'5 x {numb} = {5 * numb}')
# print(f'6 x {numb} = {6 * numb}')
# print(f'7 x {numb} = {7 * numb}')
# print(f'8 x {numb} = {8 * numb}')
# print(f'9 x {numb} = {9 * numb}')
# print(f'10 x {numb} = {10 * numb}')

# line 1
# print(f'1 x 2 = 2',end="\t")
# print(f'1 x 3 = 3',end="\t")
# print(f'1 x 4 = 2',end="\t")
# print(f'1 x 5 = 2',end="\t")

# print()

# print(f'2 x 2 = 2',end="\t")
# print(f'2 x 3 = 2',end="\t")
# print(f'2 x 4 = 2',end="\t")
# print(f'2 x 5 = 2',end="\t")
# print()

# # line 1
# for i in range(2,6):
#     print(f'1 x {i} = {1 * i}',end="\t")
# print()

# # line 2
# for i in range(2,6):
#     print(f'2 x {i} = {2 * i}',end="\t")
# print()


# for j in range(1,11):
#     for i in range(2,6):
#         print(f'{j} x {i} = {j * i}',end="\t")
#     print()
# print()

# for j in range(1,11):
#     for i in range(6,10):
#         print(f'{j} x {i} = {j * i}',end="\t")
#     print()
# print()


# Завдання 1
# Користувач вводить число. Визначити кількість цифр у цьому числі, порахувати їхню суму та середнє арифметичне. Визначити кількість нулів у цьому числі. Спілкування з користувачем організувати через меню.

# numb = int(input("Enter number :: "))
# len = 0
# sum = 0
# number_of_zero = 0
# while True:
    
#     choice = int(input('''
#             [1] - кількість цифр
#             [2] - сума цифр
#             [3] - середнє арифметичне
#             [4] - кількість нулів
#             [0] - вихід
#             --> '''))
#     if choice == 0:
#         break
#     '''
#         123 % 10 --> 3;
#         123 // 10 --> 12

#         12 % 10 --> 2;
#         1 // 10 --> 1

#         1 % 10 --> 1;
#         1 // 10 --> 0
#     '''

#     while numb != 0:
#         digit = numb % 10
#         numb //= 10

#         len += 1
#         sum += digit
#         if digit == 0:
#             number_of_zero += 1


#     match choice:
#         case 1:
#             print(f'кількість цифр = {len}')
#         case 2:
#             print(f'сума цифр = {sum}')
#         case 3:
#             print(f'середнє арифметичне = {sum / len}')
#         case 4:
#             print(f'кількість нулів = {number_of_zero}')

# Завдання 4
# Напишіть програму, яка малює драбинку висотою N, де:
'''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
'''

# line 1
# print('1',end=' ')
# print()
# for i in range(1,2):
#     print(i,end=" ")
# print()

# # line 2
# # print('1', end=' ')
# # print('2', end=' ')
# # print()
# for i in range(1,3):
#     print(i,end=" ")
# print()

# # line 3
# # print('1', end=' ')
# # print('2', end=' ')
# # print('3', end=' ')
# # print()
# for i in range(1,4):
#     print(i,end=" ")
# print()

# line = int(input("Enter number of lines :: "))
# for j in range(1, line + 1):
#     for i in range(1, j + 1):
#         print(i,end=" ")
#     print()

line = 5
'''
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''
# # line 1
# for i in range(1, 5 + 1):
#     print(i,end=" ")
# print()

# # line 2
# for i in range(1, 4 + 1):
#     print(i,end=" ")
# print()

# # line 2
# for i in range(1, 3 + 1):
#     print(i,end=" ")
# print()
# q = 0
# for j in range(line,0,-1):
#     print(' ' * q, end='')
#     q+= 2
#     for i in range(1, j + 1):
#         print(i,end=" ")
#     print()

# line = 4
'''
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1

'''
# # line 1
# print(' ' * 3 * 2,end='')
# print('1',end=' ')
# print()

# # line 2
# print(' ' * 2 * 2,end='')
# print('1',end=' ')
# print('2',end=' ')
# print('1',end=' ')
# print()

# # line 3
# print(' ' * 1 * 2,end='')
# print('1',end=' ')
# print('2',end=' ')
# print('3',end=' ')
# print('2',end=' ')
# print('1',end=' ')
# print()

# # line 3
# print(' ' * 0 * 2,end='')
# print('1',end=' ')
# print('2',end=' ')
# print('3',end=' ')
# print('4',end=' ')
# print('3',end=' ')
# print('2',end=' ')
# print('1',end=' ')
# print()

line = 7
for i in range(1, line + 1):
    print(' ' * ((line - i ) * 2), end='')
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    print()

