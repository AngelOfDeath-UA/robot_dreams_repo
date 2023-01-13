# coded: UTF-8

import json
import os.path


class JSONEngine:
    """Class for working with JSON file like Data-Base for Telephone Book"""

    def __init__(self, filename: str):
        self.filename = filename
        self.existence_file_check()

    def existence_file_check(self):
        if not os.path.isfile(self.filename) or os.stat(
                self.filename).st_size == 0:  # is there file and empty it is?
            with open(self.filename, 'a+') as created_file:
                created_file.write('{}')

    def write_to_file(self, data: dict):
        with open(self.filename, 'w') as write_file:
            json.dump(data, write_file)

    def read_from_file(self) -> dict:
        if self.filename[-5:] == ".json":
            with open(self.filename) as read_file:
                loaded_json_file = json.load(read_file)
                return loaded_json_file


class TelephoneBook(JSONEngine):
    """Class Telephone Book, can give statistic, add and delete files from Data Base"""

    _json_book_data_base_name = "book_data_base.json"

    def __init__(self, command: str, json_file_name=_json_book_data_base_name):
        super().__init__(json_file_name)
        self.command = command.split()
        self.phone_book_dict = self.read_from_file()
        self.command_init()

    def command_init(self):
        match self.command:

            case ["stats"]:
                self.command_stats()

            case ["list"]:
                self.command_list()

            case ["help"]:
                self.command_help()

            case ["exit"]:
                self.command_exit()

            case "delete", name:
                self.command_delete(name)

            case 'show', name:
                self.command_show(name)

            case 'add', name, phone:
                self.command_add(name, phone)

            case _:
                print("Не вірна команда. Для допомоги, введіть команду: help ")

    def command_stats(self):
        print(len(self.phone_book_dict))

    def command_add(self, name, phone):
        if name not in self.phone_book_dict.keys():
            self.phone_book_dict[name] = [phone]
            self.write_to_file(self.phone_book_dict)
        else:
            add_input = input(" Увага - це ім'я вже існує! \n "
                              "Натисніть 1 якщо хочете додати ще один номер \n"
                              " або 2 щоб ввести нове ім'я ")
            if add_input == '1':
                self.phone_book_dict[name].append(phone)
                self.write_to_file(self.phone_book_dict)

    def command_delete(self, name):
        self.phone_book_dict.pop(name)
        self.write_to_file(self.phone_book_dict)

    def command_list(self):
        print(self.phone_book_dict.keys())

    def command_show(self, name):
        if name in self.phone_book_dict:
            print(self.phone_book_dict[name])
        else:
            print("Контакт не знайдено.")

    def command_help(self):
        print(
            "Приклад команд: \n"
            "stats: кількість записів \n"
            "add <name> <telephone>: додати запис \n"
            "delete <name>: видалити запис за іменем (ключем)\n"
            "list: список всіх імен в книзі\n"
            "show <name>: детальна інформація по імені\n"
            "exit: вихід"
        )

    @staticmethod
    def command_exit():
        exit("Завершую роботу.")


if __name__ == "__main__":
    while True:
        telephone_book = TelephoneBook(input("Чекаю комаду: "))
