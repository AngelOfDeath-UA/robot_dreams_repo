# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

# Task 3 Custom Exception with Logging

# import logging
# from datetime import datetime
#
# class MyCustomException(Exception):
#     def __init__(self, message="Custom exception is occured"):
#         logging.basicConfig(level=logging.DEBUG, filename='exception.log')
#         self.message = message
#         self.logging()
#         super().__init__(self.message)
#     def logging(self):
#         logging.debug(f'Raised MyCustomException with massage {self.message} | Time: {datetime.now()} \n')
#
# raise MyCustomException()

# Task 3 Custom Exception with CSV

# import csv
# from datetime import datetime
#
# class MyCustomException(Exception):
#     def __init__(self, message="Custom exception is occured"):
#         self.message = message
#         self.logging()
#         super().__init__(self.message)
#     def logging(self):
#         with open('exceptions.csv', 'a+', newline='') as out_csv:
#                 writer = csv.writer(out_csv)
#                 writer.writerow(['MyCustomException', self.message , str(datetime.now())])
#
# raise MyCustomException()

