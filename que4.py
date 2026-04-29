# a = 500;
# x = int(input("Enter the amount to withdraw "));
# if(x%5==0 and x<=500):
#     print("Withdrawal successful");
#     print("Remaining balance= ", (a-x-0.5));
# else:
#     print("Enter amount in multiple of 5 or less than", a);

amount = 120;
if(amount>500):
    a500n = amount//500;
    amount = amount%500;
    print("required 500rs. notes",a500n);
if(amount>200):
    a200n = amount//200;
    amount = amount%200;
    print("required 200rs. notes",a200n);
if(amount>100):
    a100n = amount//100;
    amount = amount%100;
    print("required 100rs. notes",a100n);
if(amount>50):
    a50n = amount//50;
    amount = amount%50;
    print("required 50rs. notes",a50n);
if(amount>10):
    a10n = amount//10;
    amount = amount%10;
    print("required 10rs. notes",a10n);
