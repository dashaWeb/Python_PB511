'''
 1 - open file
 2 - read file
 3 - write file
 4 - close file 

'''

# ---------------- Read file -------------
url = r"C:\Users\kap19\Desktop\test.txt"

# fileHandler = open(url)
# print(type(fileHandler), fileHandler)
# text = fileHandler.read()
# print(text, type(text), sep='\n')
# print('Position file cursore ',fileHandler.tell())
# fileHandler.close()

# fileHandler = open(url)
# test = fileHandler.read(15)
# print(test)

# print('Position file cursore ',fileHandler.tell())
# fileHandler.seek(0)

# text = fileHandler.readline()
# print('Read line :: ', text)

# fileHandler.seek(0)
# for line in fileHandler:
#     print(line,end='')


# fileHandler.seek(0)
# text = fileHandler.readlines()
# print()
# print(text)
# print(text[-1])
# fileHandler.close()


# with open(url) as fileHandler:
#     print(fileHandler.read())


# ------------------------ Write file -------------------

# with open(r'16_files/my_app.txt', 'w') as file:
#     file.write("Hello World 2")
# with open(r'16_files/my_app.txt', 'a') as file:
#     file.write("Hello World 2\n")


# with open(r'16_files/my_app_ua.txt', 'a', encoding='utf-8') as file:
#     file.write("Привіт Світ 1!")

# with open(r'16_files/my_app_ua.txt', 'r', encoding='utf-8') as file:
#     print(file.read())