# zadacha_1
# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_hide(card):
    return '*' + card[16:]

def card_hide(card):
    for i in range(len(card)):
        if i <= 11:
            print('*', end=' ')
        else:
            print(card[i], end='')
# a=int(input('Ведите номер карты: '))
card_hide('1234456778944561')