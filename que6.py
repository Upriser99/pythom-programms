# Python program for armstrong numbers
# Python program for sum of individual digits of a number
# Python program for Range or loop



a_n = int(input("Enter a 3 digit number "))
a_n = str(a_n)
# print(int(a_n[0]))
# print(int(a_n[1]))
# print(int(a_n[2]))
digit1 = (int(a_n[0])*(int(a_n[0]))*(int(a_n[0])))
# print(digit1)
digit2 = (int(a_n[1])*(int(a_n[1]))*(int(a_n[1])))
# print(digit2)
digit3 = (int(a_n[2])*(int(a_n[2]))*(int(a_n[2])))
# print(digit3)
s = digit1+digit2+digit3;
print(s)

if(int(digit1+digit2+digit3) == int(a_n)):
    print("Its a armstrong number")
else:
    print("Its not an armstrong number")


# if(str(digit1)+str(digit2)+str(digit3)) == a_n):
#     print("Its a armstrong number")
# for i in range(0,101,2):
#     print(i);


# print(len(str(a_n)))
# a_n = str(a_n)
# digit1 = (a_n)
# print(int(a_n[0])+(int(a_n[1]))+(int(a_n[2])))
