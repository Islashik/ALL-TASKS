hours = int(input('введите часы: '))
minutes = int(input('введите минуты: '))
seconds = int(input('введите секунды: '))
hours2 = int(input('введите часы: '))
minutes2 = int(input('введите минуты: '))
seconds2 = int(input('введите секунды: '))
time1 = (hours*60*60)+(minutes*60)+seconds
time2 =(hours2*60*60)+(minutes2*60)+seconds2
print(f'Разница времени в секундах',time2 - time1)

