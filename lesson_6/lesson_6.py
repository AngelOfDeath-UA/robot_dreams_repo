# coded: UTF-8

# Phone Book 1 Version

def main(phone_book_dict, input_string):
    input_command = input_string.split()[0]

    try:
        name = input_string.split()[1]
        phone = input_string.split()[2]
    except IndexError:
        if input_command == "delete" or input_command == "add":
            print("Не вірна команда.")
            return False

        else:
            pass

    match input_command:

        case "stats":
            print(len(phone_book_dict))

        case "list":
            print(phone_book_dict.keys())

        case "help":
            print(
                "Приклад команд: \n"
                "stats: кількість записів \n"
                "add <name> <telephone>: додати запис \n"
                "delete <name>: видалити запис за іменем (ключем)\n"
                "list: список всіх імен в книзі\n"
                "show <name>: детальна інформація по імені\n"
                "exit: вихід"
            )

        case "exit":
            exit("Завершую роботу.")

        case "delete":
            phone_book_dict.pop(name)

        case 'show':
            if name in phone_book_dict:
                print(phone_book_dict[name])
            else:
                print("Контакт не знайдено.")

        case "add":
            if name not in phone_book_dict.keys():
                phone_book_dict[name] = phone
            else:
                print("Помилка: Увага це ім'я вже існує! Виберіть інше!")

        case _:
            print("Не вірна команда. Для допомоги, введіть команду: help ")


if __name__ == "__main__":

    phone_book_dict = {}

    while True:

        input_string = input("Чекаю комаду: ")

        if main(phone_book_dict, input_string) == False:
            continue

# Phone Book 2 Version (with list in dict without Exceptions)

def main(phone_book_dict, command):
    match command:

        case ["stats"]:
            print(len(phone_book_dict))

        case ["list"]:
            print(phone_book_dict.keys())

        case ["help"]:
            print(
                "Приклад команд: \n"
                "stats: кількість записів \n"
                "add <name> <telephone>: додати запис \n"
                "delete <name>: видалити запис за іменем (ключем)\n"
                "list: список всіх імен в книзі\n"
                "show <name>: детальна інформація по імені\n"
                "exit: вихід"
            )

        case ["exit"]:
            exit("Завершую роботу.")

        case "delete", name:
            phone_book_dict.pop(name)

        case 'show', name:
            if name in phone_book_dict:
                print(phone_book_dict[name])
            else:
                print("Контакт не знайдено.")

        case 'add', name, phone:
            if name not in phone_book_dict.keys():
                phone_book_dict[name] = [phone]
            else:
                add_input = input(" Увага - це ім'я вже існує! \n "
                                  "Натисніть 1 якщо хочете додати ще один номер \n"
                                  " або 2 щоб ввести нове ім'я ")
                if add_input == '1':
                    phone_book_dict[name].append(phone)
        case _:
            print("Не вірна команда. Для допомоги, введіть команду: help ")


if __name__ == "__main__":

    phone_book_dict = {}

    while True:
        input_string = input("Чекаю комаду: ").split()
        main(phone_book_dict, input_string)
