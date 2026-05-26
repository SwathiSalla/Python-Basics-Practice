a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=input("Enter choice(1/2/3/4): ")
if choice=='1':
    print(a,"+",b,"=",a+b)
elif choice=='2':
    print(a,"-",b,"=",a-b)
elif choice=='3':
    print(a,"*",b,"=",a*b)
elif choice=='4':
    if b!=0:
        print(a,"/",b,"=",a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")
