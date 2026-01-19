import re

str_1 = '123'
str_2 = '234'
str_3 = 'Lorem** 21 ipsum red'

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('12',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('12',str_2)}")
print(f"\t {str_3} \t ---> {re.search('12',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('[12]',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('[12]',str_2)}")
print(f"\t {str_3} \t ---> {re.search('[12]',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('[0-9]',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('[0-9]',str_2)}")
print(f"\t {str_3} \t ---> {re.search('[0-9]',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('[a-zA-Z0-9]',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('[a-zA-Z0-9]',str_2)}")
print(f"\t {str_3} \t ---> {re.search('[a-zA-Z0-9]',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\w',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\w',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\w',str_3)}")

match = re.search('[a-zA-Z]{3,10}\** \w+',str_3)

if match:
    print("Find by letter")
    print(match.start(), match.end(), match.group(0))
else:
    print('not found letter')


print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\w{3}$',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\w{3}$',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\w{3}$',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('^\w{3}',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('^\w{3}',str_2)}")
print(f"\t {str_3} \t ---> {re.search('^\w{3}',str_3)}")
print(f"\t {str_3} \t ---> {re.search('^[a-z]{3}',str_3)}")


print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('^[^a-z]{3}',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('^[^a-z]{3}',str_2)}")
print(f"\t {str_3} \t ---> {re.search('^[^a-z]{3}',str_3)}")



print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\W',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\W',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\W',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\W',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\W',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\W',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\d*',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\d*',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\d+',str_3)}")

print("\n\n =================== re.search(template, str) =======================\n")
print(f"\t {str_1} \t\t\t ---> {re.search('\D+',str_1)}")
print(f"\t {str_2} \t\t\t ---> {re.search('\D+',str_2)}")
print(f"\t {str_3} \t ---> {re.search('\D+',str_3)}")

str_3 ='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ultrices nec elit tempor suscipit. In hac habitasse platea dictumst. In aliquet ipsum at magna lacinia consectetur. Etiam eget augue ex. Nunc in felis ac enim tempor convallis. Nulla convallis, ligula sed rhoncus suscipit, massa purus gravida felis, pretium mollis nibh sapien at turpis. Praesent malesuada massa vitae sapien tristique vulputate. Pellentesque tristique viverra faucibus. Integer lectus lorem, tempor ut luctus quis, pellentesque et diam.'
match = re.findall(r'[ .,]\w{3}[ .,]',str_3)
print(match)
for word in match:
    print(word)

print(re.sub(r'[ .,]\w{3}[ .,]',' yellow ',str_3,count=1))


import string
import random

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

print(''.join(random.sample(string.ascii_letters,8)))
# print(''.join([1,2,3,4,5,6]))

print('Lorem'.center(50))
print(' Lorem '.center(50,'*'))
print('\tLorem\t'.expandtabs(20))
print(' Lorem '.rjust(50,'*'))
print(' Lorem '.rjust(50))
print(' Lorem '.ljust(50,'*'))
print('Lomrem'.lstrip('Lo'))
print('Lomrem'.rstrip('m'))
print('mmLomrem'.strip('m'))
print('L124'.zfill(10))


print("ttest {0:3.2f}".format(2.5658569))
print("ttest {0:4d}".format(20))