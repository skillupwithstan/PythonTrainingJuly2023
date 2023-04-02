'''
import datetime

print(dir(datetime))
print(dir(datetime.datetime))

# Get the current date and time
dtnow = datetime.datetime.now()
print(dtnow)

# Get current date
current_date = datetime.date.today()
print(current_date)

# Date object to represent a date
dt = datetime.date(2023, 12, 25)
print(dt)

# Import Only date Class
from datetime import date

dt = date(2023, 12, 25)
print(dt)

import datetime

datetime.date.today()

print(dir(datetime.datetime.day))

help(datetime)

from datetime import date

# Get current date using today() method
todays_date = date.today()

print("Today's date =", todays_date)
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)

'''
from datetime import datetime

# current date and time
dtnow = datetime.now()
print("Current DateTime:",dtnow)

t = dtnow.strftime("%H:%M:%S")
print("Time:", t)

s1 = dtnow.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = dtnow.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)