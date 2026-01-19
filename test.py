#Task 1
text = input("Введіть текст: ")

count = 0
for ch in text:
    if ch == "." or ch == "!" or ch == "?":
        count += 1

print("Кількість речень - ", count)

#Task 2
text = input("Введіть рядок: ")

text = text.lower()
text = text.replace(" ", "")

if text == text[::-1]:
    print("Паліндром")
else:
    print("Не паліндром")

#Task 3
text = input("Введіть текст: ")

text = text.replace("я", "Я")
text = text.replace("ти", "ТИ")
text = text.replace("ми", "МИ")
text = text.replace("вони", "ВОНИ")
text = text.replace("кіт", "КІТ")

print(text)



#Task 4
text = input("Введіть рядок: ")
ch1 = input("Введіть перший символ: ")
ch2 = input("Введіть другий символ: ")

pos1 = text.find(ch1)
pos2 = text.find(ch2)

if pos1 != -1 and pos2 != -1 and pos1 < pos2:
    result = text[:pos1] + text[pos2 + 1:]
    print(result)
else:
    print("Неможливо виконати")


#Task 5
text = input("Введіть текст: ")
symbols = input("Введіть набір символів: ")

words = text.split()
result = ""

for w in words:
    delete = False
    for ch in symbols:
        if ch in w:
            delete = True
    if not delete:
        result += w + " "

print(result)


#Task 6

text = input("Введіть текст: ")

words = text.split()
words.reverse()

result = ""
for w in words:
    result += w + " "

print(result)
