# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os
import re


for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


a = input("нажмите Enter - продолжить")

for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Директория {} не найдена'.format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

path = os.getcwd()
print('текущая дирректория %s' % path)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


destdir = os.path.abspath('destdir')
if not os.path.exists(destdir):
    os.makedirs(destdir)

print(destdir)