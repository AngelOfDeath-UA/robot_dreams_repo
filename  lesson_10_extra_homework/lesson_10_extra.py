# Використовуючи бібілотеку requests та endpoint https://dog.ceo/api/breeds/image/random
# написати програму, яка буде робити 5 запитів на даний ендпоінт використовуючи потоки, а отримавши response має
# записати посилання на отримані картинки в файл my_dogs.txt або зберегти картинки в директорію my_dogs
# Програма має друкувати загальний час виконання, а також час виконання кожного окремого запиту.

# coded: UTF-8
# {"status":"success","message":"https://images.dog.ceo/breeds/germanshepherd/n02106662_9292.jpg"}


import requests
from threading import Thread
from datetime import datetime


class LinkDownloader(Thread):
    def __init__(self, link: str, filename='my_dogs.txt'):
        super().__init__()
        self.link = link
        self.filename = filename
    def run(self):
        self.write_to_file()

    def get_link(self):
        get_str = requests.get(self.link, params={'key': 'value'})
        return (eval(get_str.text))['message']


    def write_to_file(self):
        with open(self.filename, 'a') as w_file:
            w_file.write(self.get_link() + '\n')

if __name__ == "__main__":

    time_start = datetime.now()

    thread1 = LinkDownloader('https://dog.ceo/api/breeds/image/random')
    thread2 = LinkDownloader('https://dog.ceo/api/breeds/image/random')
    thread3 = LinkDownloader('https://dog.ceo/api/breeds/image/random')
    thread4 = LinkDownloader('https://dog.ceo/api/breeds/image/random')
    thread5 = LinkDownloader('https://dog.ceo/api/breeds/image/random')

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print(datetime.now() - time_start)
