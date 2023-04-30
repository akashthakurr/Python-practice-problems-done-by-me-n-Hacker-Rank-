import calendar

month, day, year = map(int, input().split())
week_days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
day_name = calendar.weekday(year, month, day)
print(week_days[day_name])