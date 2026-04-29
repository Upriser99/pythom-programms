y = int(input("Enter a year to check"))
if(y%400==0 or (y%4==0 and y%100!=100)):
    print("Its a leap year");
else:
    print("Its not a leap year");