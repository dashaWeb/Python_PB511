
# "Test for"


# i = 1
# for letter in "Test for":
#     print(letter * i)
#     i+=1

# print(range(10)) # 0 1 2 3 4 5 .... 9


# for i in range(10):
#     print(i, end="\t")
# print()

# for i in range(1,10): # 1 2 3 4 5 .... 9
#     print(i, end="\t")
# print()

# for i in range(10,1,-1): # 1 3 5 7 9
#     print(i, end="\t")
# print()


# numb = int(input("Enter number :: ")) #10 {1 2 3 4 5 .. 10}
# for i in range(1, numb+1):
#     if numb % i == 0:
#         print(i, end="\t")

# Way 1
#number = int(input("Enter number :: "))
# counter = 0

# for i in range(1, number+1):
#     if number % i == 0:
#         counter+=1

# if counter == 2:
#     print("Prime")
# else:
#     print("Complex")

#Way 2
# number = int(input("Enter number :: "))
# flag = True
# for i in range(2, number):
#     if number % i == 0:
#         flag = False
#         break

# if flag:
#     print("Prime")
# else:
#     print("Complex")

#Way 3
# 100 / 50 -> 51,52,
# number = int(input("Enter number :: "))
# for i in range(2, number // 2 + 1):
#     if number % i == 0:
#         print("Complex")
#         break
# else:
#     print("Prime")

import random

# for i in range(5):
#     # print(random.randint(1,10))
#     # print(int(random.random() * 10 + 1))
#     print(random.choice("rps"))
user_counter = 0
bot_counter = 0
draw_counter = 0
while True:
    levels = 0
    bot_score = 0
    user_score = 0
    while levels < 3:
        levels+= 1
        print(F"------------------- ROUND #{levels} --------------------")
        while True:
            user = input('''
                        [s] - scissors
                        [p] - paper
                        [r] - rock
                        Enter your choise --> ''')
            if user =='s' or user == 'p' or user == 'r':
                break
            else:
                print("Error! Enter true choise")
        bot = random.choice('srp')

        print(f'''
                        User    Bot
                        [{user}]     [{bot}]
            ''')
        if user == 's' and bot == 'p' or user == 'p' and bot == 'r' or user == 'r' and bot == 's':
            user_score +=1 
        elif bot == user:
            continue
        else:
            bot_score += 1
    if user_score > bot_score:
        print("=============== Congratulations!!! ===============")
        user_counter += 1
    elif user_score == bot_score:
        print("=============== Draw!!! ===============")
        draw_counter += 1
    else:
        print("=============== Sorry!!! You Loser! ===============")
        bot_counter += 1
    
    while True:
        way = input("Restart [y] - yes; [n] - no --> ")
        if way == 'y' or way == 'n':
            break
        else:
            print("Error! Enter true choise")
    if way == 'n':
        break

print(f'''
            [User win] -- {user_counter}
            [Bot win]  -- {bot_counter}
            [Draw]     -- {draw_counter}
    ''')