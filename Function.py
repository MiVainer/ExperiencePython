def function(price):
    """Peres4itat ceny s y4etom nds"""
    nds = 13/100
    new_price = price + nds*price
    print('новая цена -', new_price)

def summa(x, y):
    s = x + y
    return s

def factorial():
    x = int(input('Введи значение факториала - !'))
    fak = 1
    for i in range(1, x+1):
        fak = fak * i
    return fak

def stroka():
    print('---------------')

print('Функция № 1')
function(110) # Вызвали функцию с величиной price = 110.
stroka()

print('Функция № 2')
x = summa(10, 20)
print(x)
stroka()

print('Функция № 3\nЗначение факториала -', factorial())
stroka()