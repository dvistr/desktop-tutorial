first=(input('Введите число: '))
sekond=(input('Введите число: '))
third=(input('Введите число: '))
if first == sekond and sekond == third:
    print('3')
elif first == sekond or sekond==third or first==third:
    print ('2')
else:
    print('0')