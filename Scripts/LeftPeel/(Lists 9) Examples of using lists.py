from re import X


# chat_text = []

# while True:
#     text = input("Enter your thoughts (Enter X to exit): ")
#     if text == "x" or text == 'X':
#         break
#     chat_text.append(text)

# print(chat_text)

# Enter your thoughts (Enter X to exit: Feeling good
# Enter your thoughts (Enter X to exit: Learning is fun
# Enter your thoughts (Enter X to exit: x
# ['Feeling good', 'Learning is fun']

# chat_text = []

# while True:
#     text = input('Enter your thoughts (Enter X to exit): ')
#     if text == "x" or text == 'X':
#         break
#     chat_text.append(text)

# for line in chat_text:
#     print(line)
# Enter your thoughts (Enter X to exit): Living large
# Enter your thoughts (Enter X to exit): Loving life
# Enter your thoughts (Enter X to exit): Hello World!
# Enter your thoughts (Enter X to exit): X
# Living large
# Loving life
# Hello World!

# chat_text = []

# while True:
#     text = input('Enter your thoughts (Enter X to exit): ')
#     if text == "x" or text == 'X':
#         break
#     chat_text.append(text)

# for i in range(0, len(chat_text)):
#     print(str(i) + " " + chat_text[i])  #This prints out the index number as well as the line of input
# Enter your thoughts (Enter X to exit): Flip flop
# Enter your thoughts (Enter X to exit): Dog mouth
# Enter your thoughts (Enter X to exit): webster
# Enter your thoughts (Enter X to exit): x
# 0 Flip flop
# 1 Dog mouth
# 2 webster

primes = []
#2, 3, 5, 6, 11, 13...

for num in range(2, 100):
    div_count = 0
    for div_by in range(2, num):
        if num % div_by == 0:
            div_count += 1
    if div_count == 0:
        primes.append(num)
print(primes) 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]



# num = 7 div_by -> 2, 3, 4, 5, 6
