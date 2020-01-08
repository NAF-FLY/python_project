while True:
    s = input('что-нибудь введите: ')
    if s=='выход':
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print('Введенная строка лостаточной длины')