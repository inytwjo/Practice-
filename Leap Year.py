year=int(input("Enter a year: "))

if(year % 4 == 0): #performing leap year, it should be divisible by 4 
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")
