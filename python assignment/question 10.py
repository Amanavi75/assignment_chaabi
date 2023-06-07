# Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

from datetime import datetime, timedelta

def get_previous_date(date, n):
    date_obj = datetime.strptime(date, '%y-%m-%d')
    
    previous_date = date_obj - timedelta(days=n)
    
    previous_date_str = previous_date.strftime('%y-%m-%d')
    
    return previous_date_str
    
date = '16-12-10'
n = 11

result = get_previous_date(date, n)
print(result)
