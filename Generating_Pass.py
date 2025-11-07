#Generating password of 18 characters

import random


letters =[]
numbers=[]
symbols=['!','#','@','$','%','&','*','?','+',')','(']


# ord('a') -> gives you the ASCII code of the 'a' character
for i in range(ord('a'), ord('z') + 1):
    letters.append(chr(i))

for i in range(1, 101):
    numbers.append(i)

Password = ''

for char in range(0,6):
    Random_letter = random.choice(letters)
    Password += Random_letter

for num in range(0,6):
    Random_number = random.choice(numbers)
    Password += chr(Random_number)

for num in range(0,6):
    Random_symbol = random.choice(symbols)
    Password += Random_symbol


print(Password)