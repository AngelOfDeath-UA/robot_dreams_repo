# coded: UTF-8

# Phone Book 1 Version

if __name__ == "__main__":

    phone_book_dict = {}

    while True:

        input_string = input("Чекаю комаду: ")
        input_command = input_string.split()[0]

        try:
            name = input_string.split()[1]
            phone = input_string.split()[2]
        except IndexError:
            pass

        match input_command:

            case "stats":
                print(len(phone_book_dict))

            case "add":
                if name not in phone_book_dict.keys():
                    phone_book_dict[name] = phone
                else:
                    print("Помилка: Увага це ім'я вже існує! Виберіть інше!")

            case "delete":
                phone_book_dict.pop(name)

            case "list":
                print(phone_book_dict.keys())

            case "show":
                print(phone_book_dict[name])

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

            case _:
                print("Не вірна команда. Для допомоги, введіть команду: help ")


# Phone Book 2 Version (with list in dict without Exceptions)


if __name__ == "__main__":

    phone_book_dict = {}

    while True:

        input_string = input("Чекаю комаду: ")
        input_command = input_string.split()[0]

        if len(input_string.split()) == 1:

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

        elif len(input_string.split()) == 2:

            name = input_string.split()[1]

            match input_command:

                case "show":
                    print(phone_book_dict[name])

                case "delete":
                    phone_book_dict.pop(name)

        elif len(input_string.split()) == 3:

            name = input_string.split()[1]
            phone = input_string.split()[2]

            match input_command:
                case "add":
                    if name not in phone_book_dict.keys():
                        phone_book_dict[name] = [phone]
                    else:
                        add_input = input(" Увага - це ім'я вже існує! \n "
                                          "Натисніть 1 якщо хочете додати ще один номер \n"
                                          " або 2 щоб ввести нове ім'я ")
                        if add_input == '1':
                            phone_book_dict[name].append(phone)
                        else:
                            continue

