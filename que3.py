a = 500;
x = int(input("Enter the amount to withdraw "));
if(x%5==0 and x<=500):
    print("Withdrawal successful");
    print("Remaining balance= ", (a-x-0.5));
else:
    print("Enter amount in multiple of 5 or less than", a);
