def reverse(text):
    return text[::-1] # вырезка из текста + -1 - это обратный порядок

def is_palindrome(text):
    return text == reverse(text) # переворачиваем текст и сравниваем с исходным 

something = input('Введите текст: ').lower()

forbidden = (',', '.', '!', '?', ';', ':', '-', ' ')

for change in something:
    if change in forbidden:
        something = something.replace(change, '')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
