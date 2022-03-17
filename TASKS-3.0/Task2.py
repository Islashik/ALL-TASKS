students = int(input('Введите количество учеников: '))
apples = int(input('Введите количество яблок: '))
coefficient = apples // students
residue = apples % students
print(f'Каждому по {coefficient} яблок(у)')
print(f'Остаток: {residue} яблок(о)')