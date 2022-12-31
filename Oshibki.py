

filname = '../21.txt'

try:
    myfile = open(filname, mode='r', encoding='koi8_r')
except Exception:
    print('Inside exception')
    print('Error found')
else:
    print('inside else')
    print(myfile.read())
finally:
    print('inside Finally')




print('==============================================')