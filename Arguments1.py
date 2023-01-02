# Библиотека используется для запуска программ из ОС

import os
import sys

os.system('ls -l > tests.txt')
os.system('cat tests.txt')
sys.exit()