numbers = [45,56,42,46,656,566534,3,3,4,4,6,87]
numbers2 = [756,76,78,785,5,4,34,2,23,3,3,65,79]
numbers3 = []
for number in numbers:
    if number not in numbers2:
       numbers3.append(number)
print(numbers3)