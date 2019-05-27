import string
import random


letters = string.ascii_letters
numbers = string.digits

num_letters = len(letters)

counter = int(input('Number of characters in password: '))
your_new_password = []
for i in range(counter):
    a = random.randint(0, 2)

    if a == 0 or a == 1:
        your_new_password.append(letters[random.randint(0, num_letters)])
    else:
        your_new_password.append(numbers[random.randint(0, 9)])

print(''.join(your_new_password),'\n')