print("calculator")
print("1.addition")
print("2.subtraction")
print("3.multification")
print("4.division")

x = int(input("enter your choise"))

a = int(input("enter first number"))
b = int(input("enter second number"))

if x == 1:
   c = a + b
   print(c)

elif x == 2:
   c = a-b
   print(c)

elif x == 3:
    c = a*b
    print(c)

elif x == 4:
    c = a/b
    print(c)

else:
    print("invalid choise")



    
