print("Enter -1 to stop the program")

while True:
    month = int(input("Enter the month (1-12): "))
    
    if month == -1:
        break
    elif month == 2:
        year = int(input("Please enter the year (e.g., 2023): "))
    
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month = 29
        else:
            days_in_month = 28
        print(f"There are {days_in_month} days in the month")
    elif month in [4, 6, 9, 11]:
        days_in_month = 30
        print(f"There are {days_in_month} days in the month")
    else:
        days_in_month = 31
        print(f"There are {days_in_month} days in the month")

