from pprint import pprint
def task_separator(task_number):
    task_number = ' ' + task_number + ' '
    txt = '|{txt:*^70}|'.format(txt=task_number)
    print(f'\n {txt}')

# 1 Task ver.2
task_separator(task_number='1 Task ver.2')

text = 'I love Python'
for i in range(42):
    pprint(text)

# 1 Task ver.1
task_separator(task_number='1 Task ver.1')

pprint(f'{text*42}')

# 2 Task
my_age_int = 25
age_in_month = my_age_int * 12
age_in_years = age_in_month // 12

# 3 Task
task_separator(task_number='3 Task')

my_name = 'Nikita'
my_age = f'“Му name is {my_name}, I’m {my_age_int} years old”'
print(my_age)

# 4 Task
task_separator(task_number='4 Task')

task_5_value = 1
print(task_5_value > my_age_int)
print(task_5_value < my_age_int)
print(task_5_value != my_age_int)
print(task_5_value == my_age_int)
print(task_5_value is my_age_int)
print(
      task_5_value != my_age_int and
      task_5_value < my_age_int or
      task_5_value > my_age_int
      )

# 5 Task
task_separator(task_number='5 Task')

a=2
b=5
c=6
d = int(str(a)+str(b)+str(c))
print(d)



