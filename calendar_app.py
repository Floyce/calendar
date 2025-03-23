import calendar

while True:
    year = int(input("Enter the year (or 0 to exit): "))
    if year == 0:  # Exit condition
        break
    month = int(input("Enter the month (1-12): "))
    print(calendar.month(year, month))
