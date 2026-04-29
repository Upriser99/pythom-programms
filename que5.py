# Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# An additional surcharge of 20% is added to the bill


unit = int(input("Enter electricity units "));
if(unit<=50):
    remaining_u = unit-50;
    amount = (unit*0.5);
    print("Charge for 1st 50 units: ", (amount+(amount/100)*20));
if(remaining_u>=100):
    amount1 = remaining_u*0.75;
    print("Charge for remaining 100 units: ", (amount1+(amount1/100)*20));