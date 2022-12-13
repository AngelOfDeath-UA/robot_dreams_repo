# coded: UTF-8

# 1 Task Version 2

import re

input_value = input('Зробіть введення значення: ')

string_regex = "^[a-zA-Zа-яА-ЯёЁЄєІіЇї]+$"
symbol_regex = "^[&^_@#\-!$%^&*()£€¥§°¢_+|~=`{}\[\]:\";'<>?,.\/\\\]+$"
number_regex = "^\d+$"

string_pattern = re.compile(string_regex)
symbol_pattern = re.compile(symbol_regex)
number_pattern = re.compile(number_regex)

for symbol in input_value:
    if number_pattern.search(symbol):
        print('Це “число”')
        if int(symbol) % 2 == 0:
            print(f'Число “{symbol}“ парне.')
        else:
            print(f'Число “{symbol}“ НЕ парне.')

    elif string_pattern.search(symbol):
        print('Це “буква”')
        if symbol.upper() == symbol:
            print(f'Буква “{symbol}“ велика.')
        else:
            print(f'Буква “{symbol}“ маленька.')

    elif symbol_pattern.search(symbol):
        print(f'Це “символ - {symbol}”')

    else:
        print(f"Як ти це зробив?")

    print("___________________")

# 1 Task Version 1

input_value = input('Зробіть введення значення: ')

for symbol in input_value:
    if symbol.isdigit():
        print('Це “число”')
        if int(symbol) % 2 == 0:
            print(f'Число “{symbol}“ парне.')
        else:
            print(f'Число “{symbol}“ НЕ парне.')
    elif not symbol.isalnum():
        print(f'Це “символ - {symbol}”')
    elif symbol.isalpha():
        print('Це “буква”')
        if symbol.upper() == symbol:
            print(f'Буква “{symbol}“ велика.')
        else:
            print(f'Буква “{symbol}“ маленька.')
    else:
        print(f"Як ти це зробив?")

    print("___________________")

# 2 Task

import time

while True:
    print("“I love Python”")
    time.sleep(4.2)


