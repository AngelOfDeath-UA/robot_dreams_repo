# coded:UTF8

# Homework 11: Task 1
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


# Homework 11: Task 2

class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self._set_url(url)
        self._set_chat_id(chat_id)

    def _set_url(self, url):
        self.url = url

    def _set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f'TG bot says {message} to chat {self.chat_id} using {self.url}')


if __name__ == "__main__":
    some_bot = Bot('Marvin')
    some_bot.say_name()
    some_bot.send_message("Hello")
    telegram_bot = TelegramBot("TG")
    telegram_bot.say_name()
    telegram_bot.send_message('Hello')
    telegram_bot._set_chat_id(1)
    telegram_bot.send_message('Hello')


# Homework 11: Task 3

class MyStr(str):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text.upper()


if __name__ == "__main__":
    my_str = MyStr('test')
    print(my_str)


# Homework 11: Task 4

class User:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if self.name == other or self.name.upper() == other:
            return True
        else:
            return False


if __name__ == "__main__":
    first_user = User('OLESII')
    second_user = User('Oleksii')
    print(first_user == second_user)


# Homework 11: Task 5

def init_func_bot(self, name):
    self.name = name


def say_name(self):
    print(self.name)


def send_message_bot(self, message):
    print(message)


def init_func_telegram(self, name, url=None, chat_id=None):
    self.name = name
    self.set_url(url)
    self.set_chat_id(chat_id)


def set_url(self, url):
    self.url = url


def set_chat_id(self, chat_id):
    self.chat_id = chat_id


def send_message_telegram(self, message):
    print(f'TG bot says {message} to chat {self.chat_id} using {self.url}')


if __name__ == "__main__":
    some_bot = type(
        "Bot",
        (),
        {
            '__init__': init_func_bot,
            'say_name': say_name,
            'send_message': send_message_bot
        }
    )

    telegram_bot = type(
        'TelegramBot',
        (some_bot,),
        {
            '__init__': init_func_telegram,
            'set_url': set_url,
            'set_chat_id': set_chat_id,
            'send_message': send_message_telegram
        }
    )

    some_bot = some_bot('Marvin')
    some_bot.say_name()
    some_bot.send_message("Hello")
    telegram_bot = telegram_bot("TG")
    telegram_bot.say_name()
    telegram_bot.send_message('Hello')
    telegram_bot.set_chat_id(1)
    telegram_bot.send_message('Hello')
