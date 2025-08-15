# Determine if a year is a leap year using nested condition statement 

year= int(input("Enter the year :"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year," is a Leap year")
        else:
            print(year," is not a Leap year")
    else:
        print(year," is Leap year")
else:
    print(year,"is not a leap year")