from typing import final

weight = float(input('Введите ваш вес: '))
for number in range(15):
    weight += 1
    moon_weight = weight * 0.165
    number += 1
    print(f'{number} год. {moon_weight} кг')

