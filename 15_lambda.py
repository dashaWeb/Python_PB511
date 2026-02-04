

def printMessage():
    print("Hello World")

def lmbMessage():print("Hello World")

lmbMessage()

def sum_(a,b):
    return a + b

print(sum_(2,5))

def lmbSum(a,b): return a + b

print(lmbSum(2,5))

''''''

import random

numbers = [random.randint(-20,20) for i in range(10)]
def printList(list_, prompt= ''):
    print(prompt, end='\t')
    for item in list_:
        print(item, end = '\t')
    print()



def revMinus(n):
    if n > 0:
        return n * -1
    return n



def revMinusList(list_):
    clone = list_.copy()
    for i in range(len(clone)):
        clone[i] = revMinus(clone[i])
    return clone

print('='*50, '\n\n')
printList(numbers, 'Before list :: ')

clone = revMinusList(numbers)
printList(clone, 'After  list :: ')

print('\n\n','='*50, '\n\n')

def test(n):
    return n**2

clone_2 = list(map(test,clone))
print(clone_2)
printList(clone_2, 'After  list :: ')

clone_2 = list(map(lambda x: x * 2 ,clone))
printList(clone, 'Before  list :: ')
printList(clone_2, 'After   list :: ')

print('\n\n','='*50, '\n\n')

sales = [random.randint(100,1000) for i in range(10)]
printList(sales, 'Start sale :: ')
sales = map(lambda x: x - (x *.10), sales)
printList(sales, 'End   sale :: ')


# numb = input("Enter numb :: ").split()
# numb = list(map(int, numb))
# print(sum(numb))
print('\n\n','='*50, '\n\n')


sales = [random.randint(-20,20) for i in range(10)]
printList(sales, 'Start before filter :: ')
sales = list(filter(lambda x: x > 0 and x < 10,sales))
printList(sales, 'Start after  filter :: ')
print('\n\n','='*50, '\n\n')
# def swap(a,b):
#     a,b = b, a
#     print(a,b)

# a = 2
# b = 5

# print('a :: ', a, "\t b :: ", b)
# swap(a,b)
# print('a :: ', a, "\t b :: ", b)

# revMinusList(numbers)
# printList(numbers)

test_ = ['test','anhhhhbs','HHH',"khhdjd"]
print(test_)
test_ = sorted(test_, key= lambda x: len(x))
print(test_)