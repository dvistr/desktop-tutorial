first=(input('Введите число: '))
sekond=(input('Введите число: '))
third=(input('Введите число: '))
if first == sekond and sekond == third:
    print('3')
elif first == sekond or sekond==third or first==third:
    print ('2')
#elif not first == sekond and not sekond == third:
    print('0')
else:
    print('0')