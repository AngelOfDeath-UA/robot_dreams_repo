# coded: UTF-8

# Task 1 Time Decorator

# import time
# from datetime import datetime
#
#
# def time_decorator(func):
#     def time_track(num):
#         print(func)
#         print(datetime.now())
#         func(num)
#
#     return time_track
#
#
# @time_decorator
# def myfunc1(i):
#     x = i ** 10000
#
#
# @time_decorator
# def myfunc2(x):
#     x += 10
#     time.sleep(3)
#
#
# if __name__ == "__main__":
#     myfunc1(100)
#     myfunc2(30)

# Task 1 Time Decorator with Logging

# import time
# import logging
# from datetime import datetime
#
#
# def time_decorator(func):
#     def time_track(num):
#         logging.debug(f'Name func: {func} | Time: {datetime.now()}')
#         func(num)
#
#     return time_track
#
#
# @time_decorator
# def myfunc1(i):
#     x = i ** 10000
#
#
# @time_decorator
# def myfunc2(x):
#     x += 10
#     time.sleep(3)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG, filename='time_decorator.log')
#     myfunc1(100)
#     myfunc2(30)

# Task 2 Custom Exception Class

# class MyCustomException(Exception):
#     def __init__(self, message="Custom exception is occured"):
#         self.message = message
#         super().__init__(self.message)
#
#
# raise MyCustomException()

# Task 3 Custom Context Manager

# file_name = 'test.txt'
#
# with open(file_name) as file:
#     for line in file:
#         print('=' * 10)
#         print(line)

# Task 4 Custom Context Manager with try|except|else

# def custom_context_manager(file_name):
#     try:
#         file = open(file_name)
#     except FileNotFoundError as exp:
#         print(f'File {exp.filename} exists!')
#     except Exception as exp:
#         print(f'An error occurred: {exp}')
#     else:
#         try:
#             for line in file:
#                 print('=' * 10)
#                 print(line)
#         except UnicodeDecodeError as exp:
#             print(f'Inside file {file_name} error with UTF-8!')
#         except Exception as exp:
#             print(exp)
#         file.close()
#
#
# file_name = 'test.txt'
# custom_context_manager(file_name)
