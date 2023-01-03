# Достаём все емайл из текстового документа

import re

filename = "/home/mihail/PycharmProjects/4.txt"
resultfilename = "/home/mihail/PycharmProjects/4result.txt"
inputfile = open(filename, mode='r', encoding='latin-1')
resultfile = open(resultfilename, mode='w', encoding='latin-1')
mytext = inputfile.read()


lookfor = r"[\w.-]+@[A-Za-z-]+.[\w]+"


results = re.findall(lookfor, mytext)

for i in results:
    print(i)