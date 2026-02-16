
# number = input('Enter number :: ')

# if number.isdigit():
#     number = float(number)
#     print(number, type(number))
# else:
#     print("Error")

# try:
#     number = int(input('Enter number :: '))
#     print(f'Result :: {number}')
#     print('Finally program')
# except ValueError:
#     print('Error number !!!!')
# else:
#     print('Run block else')
# finally:
#     print('Run block finally')


# print('End')
# try:
#     numb_1 = int(input('Enter number :: '))
#     numb_2 = int(input('Enter number :: '))
#     print(f'{numb_1} / {numb_2} = {numb_1/numb_2}')
# except ValueError as ex:
#     print('Value error',ex)
# except ZeroDivisionError as ex:
#     print('ZeroDivision Error',ex)
# except Exception as ex:
#     print('Exception Error',ex)

# print('Finally program')
# while True:
#     try:
#         numb_1 = int(input('Enter number :: '))
#         numb_2 = int(input('Enter number :: '))
#         print(f'{numb_1} / {numb_2} = {numb_1/numb_2}')
#         break
#     except (ValueError,ZeroDivisionError) as ex:
#         print('Value error or ZeroDivisionError',ex)
#     except Exception as ex:
#         print('Exception Error',ex)

# print('Finally program')


def printNumb(numb):
    if numb < 0:
        raise ValueError('number < 0')
    if numb > 10_000:
        raise OverflowError('number > 10_000')
    print(f'Ok --> {numb}')

try:
    printNumb(50)
except ValueError as ex:
    print('Error ', ex)
except Exception as ex:
    print('Error ', ex)

print('Finally program')

def division(a,b):
    try:
        print(f'{a} / {b} = {a / b}')
    except Exception as ex:
        print('ZeroDivisionError ', ex)


division('5',0)

print('Finally program')

