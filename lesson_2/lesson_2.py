# coded: UTF-8
def is_even(number):
    """
    Function return bool value:
    True if param == Even
    False if param == Not Even
    """
    return int(number) % 2 == 0


if __name__ == "__main__":

    value = input('Зробіть введення значення: ')
    try:
        if type(int(value)) == int or type(int(value)) == float:
            print('Ведений текст - “число”.')

            if is_even(number=value):
                print(f'Число {int(value)} Є парним.')
            else:
                print(f'Число {int(value)} НЕ є парним.')

    except ValueError as err_value_is_string:
        """
        Catch Exception:
        ValueError: invalid literal for int()
        """
        if type(value) == str:
            print('Ведений текст - “слово”.')
            print(f'Довжина слова "{value}" - {len(value)} букви.')
