age = int(input('Введите свой возраст: '))
if age % 2 == 0:
    for number in range(0,age + 1,2):
        print(number)
else:
    for number in range(1,age + 1,2):
        print(number)

