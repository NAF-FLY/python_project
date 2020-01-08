x = 50

def func():
    global x

    print('х равен', x)
    x = 2
    print('3аменяем глобальное значение x на', x)

func()
print('Значение х составляет', x)    