import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

cal = calendar.monthcalendar(year, month)

print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day != 0:
            print("{:2d}".format(day), end=' ')
        else:
            print("  ", end=' ')
    print()
