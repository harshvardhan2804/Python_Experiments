
daysOfWeek =["sunday","monday","tuuesday","wednesday","thursday","friday","saturday"]

presentDay = int(input("Enter current day code:"))

daysToAdd =  int(input("Enter Number of days to add:"))

ans = daysToAdd%7 + presentDay

print(daysOfWeek[ans])