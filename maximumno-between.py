A = int(input("Enter 1st number"))
B = int(input("Enter 2nd number"))
C = int(input("Enter 3rd number"))
if(A>B and A>C):
    print("The greatest number is A", A)
elif(B>C):
    print("The greatest number is B", B)
else:    
    print("The greatest number is C", C)