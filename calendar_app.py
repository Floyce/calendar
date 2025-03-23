import calendar

year = int(input("Enter the starting year: "))
           
for month in range(1, 13):
        
    #print
    print(calendar.month(year, month))