# coded: UTF-8

# 2 Task with CSV

# import time
# import csv
# from datetime import datetime
#
#
# def time_decorator(func):
#     def time_track(num):
#         with open('timetrack.csv', 'a+', newline='') as out_csv:
#             writer = csv.writer(out_csv)
#             writer.writerow([str(func), str(datetime.now())])
#             func(num)
#
#     return time_track
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

# 2 Task with Logging

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
#     logging.basicConfig(level=logging.DEBUG, filename='timetrack.log')
#     myfunc1(100)
#     myfunc2(30)
