
# def showMessage(age = 0, id = 0, phone = "nonPhone", name = 'None'):
#     print(f"Hello {name}; \t Age :: {age}; \t Id - {id} \t phone - {phone}")


# showMessage(18)
# showMessage(20)
# showMessage(16,"Olia")
# showMessage(16,111,'4444',"Olia")
# showMessage(16,name='Pavlo')


# def sum(a,b):
#     return a + b


# res = sum(5,7) / 2
# print(res)



def sum_(a,b):
    return a + b

def sub_(a,b):
    return a - b

def mult_(a,b):
    return a * b

def div_(a,b):
    if b == 0:
        print("Error :: ZeroDivisionError")
        return 
    return a / b


def calculate(a,b,op):
    match op:
        case '+':
            return sum_(a,b)
        case '-':
            return sub_(a,b)
        case '*':
            return mult_(a,b)
        case '/':
            return div_(a,b)
    print('Error! Not found operation!!')




print(f' 2 + 5 = {calculate(2,5,'+')}')
print(f' 2 - 5 = {calculate(2,5,'-')}')
print(f' 2 * 5 = {calculate(2,5,'*')}')
print(f' 2 / 5 = {calculate(2,5,'/')}')
print(f' 2 ! 5 = {calculate(2,5,'!')}')


# Task 10

def isLeap(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    # return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def getDaysOfMonth(month, year):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 29 if isLeap(year) else 28


def nextDate(day, month, year):
    day += 1
    if day > getDaysOfMonth(month,year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return f'{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}'

print(f'31.03.2004 --> {nextDate(31,3,2004)}')
print(f'28.02.2004 --> {nextDate(28,2,2004)}')
print(f'28.02.2005 --> {nextDate(28,2,2005)}')
print(f'31.12.2004 --> {nextDate(31,12,2004)}')
print(f'30.04.2004 --> {nextDate(30,4,2004)}')




