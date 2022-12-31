# Ищем строки в которых повторяется текст, или вводимые нами буквы. Выводим строки в отдельный текстовый файл.


inputfile = '../2.txt' # взять файл на дрректорию выше
outputefile = '../vivod.txt' # Вывести сюда выборку строк

password_tolookfor = str(input('Введи текст для поиска - '))

myfile = open(inputfile, mode='r', encoding='koi8_r') #mode=r - чтение
myfile1 = open(outputefile, mode='w', encoding='koi8_r') #mode=w - запись

for num, line in enumerate(myfile, 1): #одновременно выводим содержимое myfile и нумеруем его num-enumerate
    if password_tolookfor in line:
            print("Line № " + str(num) + "  " + line.strip()) #strip позволяет убрать все лишние пробелы
            myfile1.write("Found password: " + line)

myfile.close()
myfile1.close()
