# coded: UTF-8

import re
import os


class OperationsWithFile:

    def __init__(self, filename: str):
        self.filename = filename
        self.result_filename = 'new_file.txt'
        try:
            os.remove(self.result_filename)
        except FileNotFoundError:
            pass

    def open_file(self):
        try:
            with open(self.filename, mode='r', encoding='UTF8') as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            exit("Sorry there's no such file in path to read from.")

    def write_to_new_file(self, line):
        with open(self.result_filename, mode='a', encoding='UTF8') as new_file:
            new_file.write(line)

    def change_old_to_new_file(self):
        save_result_mode = input(f'If you want save result in new file named {self.result_filename} print 1 \n'
                                 f'If you want to save result to file {self.filename} print 2\n'
                                 f'Your input: ')
        if int(save_result_mode) == 2:
            os.remove(self.filename)
            os.rename(self.result_filename, self.filename)
        else:
            print(f'Sorry, you entered incorrect input. But we save your result to new file '
                  f'named: {self.result_filename}')


class MailChanger(OperationsWithFile):
    def __init__(self, mode: int, filename):
        super().__init__(filename)
        self.mail_pattern = re.compile(r'\w+@\w+.\w+')
        self.mode = mode
        self.mode_definition()

    def mode_definition(self):
        if self.mode == 1:
            self.mail_definition_ver_1()
        elif self.mode == 2:
            self.mail_definition_ver_2()
        else:
            exit('Mode version not available')
        self.change_old_to_new_file()

    def mail_definition_ver_1(self):

        for line in self.open_file():
            find_match = re.search(self.mail_pattern, line)
            if find_match:
                line = line.replace(find_match.group(), '*@*')
            self.write_to_new_file(line)

    def mail_definition_ver_2(self):

        for line in self.open_file():
            find_match = re.search(self.mail_pattern, line)
            if find_match:
                first_letter = find_match.group()[0]
                last_letter = find_match.group()[-1]
                new_mail_value = f'{first_letter}***@****{last_letter}'
                line = line.replace(find_match.group(), new_mail_value)
            self.write_to_new_file(line)


if __name__ == "__main__":
    input_mode = int(input('Write 1 if you want change all email in file to *@* \n'
                           'Or write 2 if you want change all email in file to X***@****X where X is first and last '
                           'letters\n'
                           'Your input: '))
    input_filename = input('Print filename with file extension which you want read (example: test.txt)\n'
                           'Your input: ')
    MailChanger(mode=input_mode, filename=input_filename)
