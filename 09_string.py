
# word = 'Blue'

# print('Length word :: ',len(word))
# print(word[len(word) - 1])
# print(word[0])

# word[0] = 'R' # error

# clone_word = "R"
# for i in range(1,len(word)):
#     clone_word += word[i]

# print(clone_word)

# print(word[-1])


line = "HyperText Markup Language"

# [start:stop:step]
print("\n\n")
print(line)
print(line[5:15:2])
print(line[5::2])
print(line[::2])
print(line[:15])
print(line[::-1])
print("\n\n")

print("\n\n")
print(ord('A')) 
# A - 65; a = 97
print(chr(ord('F') + 32))
print("\n\n")


print(f'Test line [{line*2}]')
print('{0} test {0} method {1} format {0}'.format('red','blue'))

print("\n\n")

print(r'\n - Enter; \t - Tab')

url = r"C:\Users\DEVOPS\tesktop\Python_PB511\08_helper_home.py"

print("\n\n")

print('Abc' == 'abc')
print('abd' == 'abc')
print('abc' == 'abc')
print('abd' > 'abc')

print(line)
print('a' in line)
print('Hyper' in line)
print('Hyper text' not in line)


print("\n\n")

number = '1245214'
letters = 'hfhfhjd'
line = "Lorem ipsum emet dolor"
word = "BANANA"
letDig = 'hdh464jgjhg'

# лише букви або цифри
print("================== isalnum()   ================")
print('\t', number, '\t -------> ', number.isalnum())
print('\t', letters, '\t -------> ', letters.isalnum())
print('\t', line, '\t -------> ', line.isalnum())
print('\t', word, '\t -------> ', word.isalnum())
print('\t', letDig, '\t -------> ', letDig.isalnum())
print("\n\n")

# лише букви
print("================== isalpha()   ================")
print('\t', number, '\t -------> ', number.isalpha())
print('\t', letters, '\t -------> ', letters.isalpha())
print('\t', line, '\t -------> ', line.isalpha())
print('\t', word, '\t -------> ', word.isalpha())
print('\t', letDig, '\t -------> ', letDig.isalpha())
print("\n\n")

# цифри
print("================== isdigit()   ================")
print('\t', number, '\t -------> ', number.isdigit())
print('\t', letters, '\t -------> ', letters.isdigit())
print('\t', line, '\t -------> ', line.isdigit())
print('\t', word, '\t -------> ', word.isdigit())
print('\t', letDig, '\t -------> ', letDig.isdigit())
print("\n\n")

# space
print("================== isspace()   ================")
print('\t', number, '\t -------> ', number.isspace())
print('\t', letters, '\t -------> ', letters.isspace())
print('\t', line, '\t -------> ', line.isspace())
print('\t', word, '\t -------> ', word.isspace())
print('\t', letDig, '\t -------> ', letDig.isspace())
print('\t', '   ', '\t -------> ', '     '.isspace())
print("\n\n")

# перевірка букв на нижній регістр
print("================== islower()   ================")
print('\t', number, '\t -------> ', number.islower())
print('\t', letters, '\t -------> ', letters.islower())
print('\t', line, '\t -------> ', line.islower())
print('\t', word, '\t -------> ', word.islower())
print('\t', letDig, '\t -------> ', letDig.islower())
print('\t', '   ', '\t -------> ', '     '.islower())
print("\n\n")

print("================== isupper()   ================")
print('\t', number, '\t -------> ', number.isupper())
print('\t', letters, '\t -------> ', letters.isupper())
print('\t', line, '\t -------> ', line.isupper())
print('\t', word, '\t -------> ', word.isupper())
print('\t', letDig, '\t -------> ', letDig.isupper())
print('\t', '   ', '\t -------> ', '     '.isupper())
print("\n\n")


print("================== istitle()   ================")
print('\t', number, '\t -------> ', number.istitle())
print('\t', letters, '\t -------> ', letters.istitle())
print('\t', line, '\t -------> ', line.istitle())
print('\t', word, '\t -------> ', word.istitle())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.istitle())
print('\t', letDig, '\t -------> ', letDig.istitle())
print('\t', '   ', '\t -------> ', '     '.istitle())
print("\n\n")



print("================== lower()   ================")
print('\t', number, '\t -------> ', number.lower())
print('\t', letters, '\t -------> ', letters.lower())
print('\t', line, '\t -------> ', line.lower())
print('\t', word, '\t -------> ', word.lower())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.lower())
print('\t', letDig, '\t -------> ', letDig.lower())
print('\t', '   ', '\t -------> ', '     '.lower())
print("\n\n")


print("================== upper()   ================")
print('\t', number, '\t -------> ', number.upper())
print('\t', letters, '\t -------> ', letters.upper())
print('\t', line, '\t -------> ', line.upper())
print('\t', word, '\t -------> ', word.upper())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.upper())
print('\t', letDig, '\t -------> ', letDig.upper())
print('\t', '   ', '\t -------> ', '     '.upper())
print("\n\n")

print("================== title()   ================")
print('\t', number, '\t -------> ', number.title())
print('\t', letters, '\t -------> ', letters.title())
print('\t', line, '\t -------> ', line.title())
print('\t', word, '\t -------> ', word.title())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.title())
print('\t', letDig, '\t -------> ', letDig.title())
print('\t', '   ', '\t -------> ', '     '.title())
print("\n\n")

print("================== capitalize()   ================")
print('\t', number, '\t -------> ', number.capitalize())
print('\t', letters, '\t -------> ', letters.capitalize())
print('\t', line, '\t -------> ', line.capitalize())
print('\t', word, '\t -------> ', word.capitalize())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.capitalize())
print('\t', letDig, '\t -------> ', letDig.capitalize())
print('\t', '   ', '\t -------> ', '     '.capitalize())
print("\n\n")


print("================== capitalize()   ================")
print('\t', number, '\t -------> ', number.swapcase())
print('\t', letters, '\t -------> ', letters.swapcase())
print('\t', line, '\t -------> ', line.swapcase())
print('\t', word, '\t -------> ', word.swapcase())
print('\t', 'Lorem Ipsum', '\t -------> ', 'Lorem Ipsum'.swapcase())
print('\t', letDig, '\t -------> ', letDig.swapcase())
print('\t', '   ', '\t -------> ', '     '.swapcase())
print("\n\n")


line = "ipsum Lorem ipsum emet ipsum dolor"
print("================== find(substr, startindex = default, endindex = default)   ================")
# index = line.find('ipsum')
# print('\t', line, '\t ----> index :: ', line.find('ipsum'), 'value :: ', line[index:index + len('ipsum')])
print('\t', line, '\t ----> ', line.find('ipsum',0))
print('\t', line, '\t ----> ', line.find('ipsum', 1))
print('\t', line, '\t ----> ', line.find('ipsum',13))
print('\t', line, '\t ----> ', line.find('ipsum',24))


print("\n\n")
print("================== find(substr, startindex = default, endindex = default)   ================")

index = -1
while True:
    index = line.lower().find('ipsum',index + 1)
    if index == -1:
        break
    print(f"Index :: {index}")

print("\n\n")


print("================== rfind(substr, startindex = default, endindex = default)   ================")

print('\t', line, '\t ----> ', line.rfind('ipsum',0))
print('\t', line, '\t ----> ', line.rfind('ipsum',0, 23))
print('\t', line, '\t ----> ', line.rfind('ipsum',0, 12))
print('\t', line, '\t ----> ', line.rfind('ipsum',0, 0))



print("================== index(substr, startindex = default, endindex = default)   ================")

print('\t', line, '\t ----> ', line.index('ipsum',0))
print('\t', line, '\t ----> ', line.index('ipsum', 1))
print('\t', line, '\t ----> ', line.index('ipsum',13))
# print('\t', line, '\t ----> ', line.index('ipsum',24))

print("================== rindex(substr, startindex = default, endindex = default)   ================")

print('\t', line, '\t ----> ', line.rindex('ipsum',0))
print('\t', line, '\t ----> ', line.rindex('ipsum',0, 23))
print('\t', line, '\t ----> ', line.rindex('ipsum',0, 12))
# print('\t', line, '\t ----> ', line.rindex('ipsum',0, 0))


print("================== count(substr)   ================")
print('\t', line, '\t ----> ', line.count('ipsum'))
print('\t', line, '\t ----> ', line.lower().count('l'))

print("================== replace(substr)   ================")
print('\t', line, '\t ----> ', line.replace('ipsum','red'))
print(line)
line = line.replace('ipsum','red')
print(line)

# 1 2 3 4 5
# test = input('Enter number --> ').split()
# sum = 0



# for i in test:
#     sum += int(i)

# print(sum)


date = '22.03.2026'.split('.')
print(date[0])

