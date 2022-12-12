# coded: UTF-8

# 1 Task

import re

input_value = input('Зробіть введення значення: ')

string_regex = "^[a-zA-Zа-яА-ЯёЁЄєІіЇї]+$"
symbol_regex = "^[&^_@#\-!$%^&*()£€¥§°¢_+|~=`{}\[\]:\";'<>?,.\/\\\]+$"
number_regex = "^\d+$"

string_pattern = re.compile(string_regex)
symbol_pattern = re.compile(symbol_regex)
number_pattern = re.compile(number_regex)

if len(input_value) == 1:
    if number_pattern.search(input_value):
        print('Це “число”')
        if int(input_value) % 2 == 0:
            print(f'Число “{input_value}“ парне.')
        else:
            print(f'Число “{input_value}“ НЕ парне.')

    elif string_pattern.search(input_value):
        print('Це “буква”')
        if input_value.upper() == input_value:
            print(f'Буква “{input_value}“ велика.')
        else:
            print(f'Буква “{input_value}“ маленька.')

    elif symbol_pattern.search(input_value):
        print('Це “символ”')
else:
    print('Введіть один символ або літеру або символ.')

# 2 Task

import time

while True:
    print("“I love Python”")
    time.sleep(4.2)


