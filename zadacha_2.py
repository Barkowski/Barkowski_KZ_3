# zadacha_2
# Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrom(a):
    a = input('Введите слово Палиндром: ')
    b = a[::-1]
    if b == a:
        return True
    else:
        return False
print(palindrom('a'))


