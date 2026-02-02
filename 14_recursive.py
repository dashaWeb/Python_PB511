'''
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1
0! = 1
'''


def factor(numb):
    if numb == 1 or numb == 0:
        return 1
    return numb * factor(numb-1)

# print(factor(5))

'''
2^4 -> 2 * 2^3
2^3 -> 2 * 2^2
2^2 -> 2 * 2^1
2^1 -> 2
'''
def power(numb, step):
    if step == 1:
        return numb
    return numb * power(numb, step - 1)

# print(power(11,2))

'''
sum(1234) -> 4 + sum(123)
sum(123) -> 3 + sum(12)
sum(12) -> 2 + sum(1)
sum(1) -> 1 + sum(0)
sum(0) -> 0
'''

# def sum_(numb):
#     if numb < 10:
#         return numb
#     return numb % 10 + sum_(numb // 10)

def sum_(numb, sum = 0):
    if numb == 0:
        return sum
    sum += numb % 10
    return sum_(numb // 10, sum)

print(sum_(9524))