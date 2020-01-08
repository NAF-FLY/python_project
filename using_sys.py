import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

if __name__ == '__main__':
    print('Эта програма запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')