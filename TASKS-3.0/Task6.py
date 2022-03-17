word = input('напишите слово: ')
pal = word[::-1]
if word == pal:
    print('Это полиндром!')
elif word != pal:
    print('Не является полиндромом!')