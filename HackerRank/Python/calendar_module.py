import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2021))

# bring the day of the week
n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
# input 08 12 2021

