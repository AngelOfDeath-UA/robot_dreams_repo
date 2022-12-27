# coded: UTF-8

# 1. Task fibonacci generator

def fibonacci_generator():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


if __name__ == "__main__":

    result = None
    number = -1
    fibo_gen = fibonacci_generator()

    if number >= 0:
        for i in range(number - 1):
            result = fibo_gen.__next__()
        print(result)
    else:
        print('Число має бути позитивне.')


# 2. Task fibonacci iterator

def fibonacci(num):
    if num >= 0:
        first = 0
        second = 1
        result = 0

        for i in range(num + 1):
            result = first
            temp = first
            first = second
            second = temp + second

        print(result)


fibonacci(9)


# 2. Task fibonacci iterator class

class Fibonachi:
    '''Итератор, который возвращает последнее число последовательности Фибоначчи'''

    def __init__(self, max_value):
        self.counter = max_value
        self.curFib = 0
        self.nextFib = 1
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.counter == 0:
                raise StopIteration
            else:
                self.counter -= 1
                self.curFib, self.nextFib = self.nextFib, self.curFib + self.nextFib
                self.result = self.curFib
        except StopIteration:
            return self.result


if __name__ == "__main__":

    result = 0
    number = 9
    fibo_gen = Fibonachi(number)

    if number >= 0:
        for i in range(number + 1):
            result = fibo_gen.__next__()
    else:
        print('Число має бути позитивне.')

    print(result)


# 3. Task fibonacci recursion

def fibonacci(num):
    if num < 0:
        print('Число має бути позитивне.')
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    number = 9
    print(fibonacci(number))


# 4. Task factorial recursion

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


number = 5
print(factorial(number))
