import re
mytext = open('/home/mihail/PycharmProjects/3.txt')
x = mytext.read()

"""
\d - любая цифра 0-9
\D - любой символ, не цифра
\w - любой алфавитный символ [A-Z, a-z]
\W - любой не алфавитный символ
\s - пробел

[0-9]{3} - 3 цифры подряд от 0 о 9
[A-Z]{2} - 2 прописные буквы подряд

"""
textlookfor = fr"{input('Введи маску для поиска - ')}"
allresults = re.findall(textlookfor, x)
print('Вот что я нашёл: '+ str(allresults))