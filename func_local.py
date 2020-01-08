x = 50

def func(x):
    print('х равен', x)
    x = 2
    print('3амена локального x на', x)

func(x)
print('x по прежнему', x)    