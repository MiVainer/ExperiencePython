list1 = ['dad', 'mom', 'brother', 'sister']
list1.append('a') #добавляем один элемент в конце списка
print('1) ', list1)
list1.extend(['p', 'r', 's']) #добавляем несколько элементов в конец списка
print('2) ', list1)
list1.insert(2, 'W') #добавляем элемент в произвольную позицию с индексом 2 (в данном примере)
print('3) ', list1)
list1.remove('mom') #удаляем из списка выбранный элемент по названию
print('4) ', list1)
del list1[3] #удаляем из списка выбранный элемент по индексу
print('5) ', list1)
NewList1 = list1.pop() #извлекаем из списка последний элемент, и присваиваем его переменной NewList1
print('6) ', NewList1)
print('7) ', list1)