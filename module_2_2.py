first=(input('Введите число: '))
sekond=(input('Введите число: '))
third=(input('Введите число: '))
if first == sekond and sekond == third:
    print('3')
if first == sekond or sekond==third or first==third:
    print ('0')
if not first == sekond and not sekond == third:
    print('2')