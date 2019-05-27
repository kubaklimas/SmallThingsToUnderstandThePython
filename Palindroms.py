a = input('Your word: ')

str1 = a[::1]

str_reverse = a[::-1]
print('Reversed word:',str_reverse)

if str1 == str_reverse:
    print('True')

else:
    print('False')