

'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''

# # line 1
# print('*' * 1, end='')
# print(' ' * 8, end='')
# print('*' * 1, end='')
# print()


# # line 2
# print('*' * 2, end='')
# print(' ' * 6, end='')
# print('*' * 2, end='')
# print()

# # line 3
# print('*' * 3, end='')
# print(' ' * 4, end='')
# print('*' * 3, end='')
# print()

# # line 4
# print('*' * 4, end='')
# print(' ' * 2, end='')
# print('*' * 4, end='')
# print()

# # line 4
# print('*' * 5, end='')
# print(' ' * 0, end='')
# print('*' * 5, end='')
# print()

# q = 10
# for i in range(1,5+1):
#     q-=2
#     print('*' * i, end='')
#     print(' ' * q, end='')
#     print('*' * i, end='')
#     print()

# for i in range(4,0,-1):
#     q+=2
#     print('*' * i, end='')
#     print(' ' * q, end='')
#     print('*' * i, end='')
#     print()

line = int(input("Enter number line --> "))
star = 0
space = line
flag = True
for i in range(1,line):
    if flag:
        star += 1
        space -= 2
    else:
        star-=1
        space+=2
    if star == line//2:
        flag = False
    print('*' * star, end='')
    print(' ' * space, end='')
    print('*' * star, end='')
    print()

