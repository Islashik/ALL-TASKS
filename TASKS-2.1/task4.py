word = input('Введите любые слова из букв в нижнем и верхнем регистре: ')
counter_for_upper = 0
counter_for_lower = 0
for letter in word:
    if letter.isupper():
        counter_for_upper += 1
    elif letter.islower():
        counter_for_lower += 1
sum = counter_for_upper + counter_for_lower
percent_big = (counter_for_upper * 100) // sum
percent_small = (counter_for_lower * 100) // sum 
print(f'Верхний регистр: {percent_big}%, Нижний регистр: {percent_small}%')
