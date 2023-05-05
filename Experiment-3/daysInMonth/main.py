

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def monthGuess(num):
    if num == 1 or num == 3 or num == 5 or num == 7 or num==8 or num == 10 or num==12:
        return True
    else:
        return False

def daysInMonth(month,year):
     if(is_leap_year(year)):
         if month==2:
             return 29
         elif monthGuess(month):
             return 31
         else:
             return 30


month = int(input("Enter month of the year"))
year = int(input("Enter year: "))

print(daysInMonth(month,year))
