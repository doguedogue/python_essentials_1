def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0

    if days_in_month(year, month) == None or day < 1 or day > days_in_month(year, month):
        return None
    for m in range(1, month+1):
        if month == m:
            md = day
        else:
            md = days_in_month(year, m)
        days += md
    return days

print(day_of_year(2000, 2, 22))