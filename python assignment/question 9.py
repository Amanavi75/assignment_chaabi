#Write a func that takes 3 args:
#from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

    date_diff = abs((from_date_obj - to_date_obj).days)
    
    if date_diff < difference:
        return True
    else:
        return False

from_date = '21-01-01'
to_date = '21-01-10'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)
