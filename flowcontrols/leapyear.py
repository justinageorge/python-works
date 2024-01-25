year=2100
if (year%100==0 and year%400==0):
    print(f"{year} is a leap year")
elif (year%100!=0 and year%4==0):
    print(f"{year} is a leap year")    
else:
    print("not a leap year")    