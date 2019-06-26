def is_leap(year):
    leap = False
    if (not(year%4) and ((year%100) or not(year%400))):
        return True
    else:
        return False
