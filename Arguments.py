import sys

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == '/?': # 0 аргумент это название самого файла программы, 1 и т.д. вводятся вручную при запуске файла
        print('Help requested')
    print('Arguments entered: ' + str(sys.argv[1:]))
else:
    print('Arguments not provided')