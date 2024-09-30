print("CACULATOR")

a = int(input("Enter the First Number = "))
b = int(input("Enter the Second Number = "))
ch = input("Enter the Operator (+,-,*,/) ")

if ch == "+":
    print(a,"+",b,"=" ,a+b)

elif ch == "-":
    print(a,"-",b,"=" ,a-b)

elif ch == "*":
    print(a,"X",b,"=" ,a*b)
    
elif ch == "/":
    print(a,"/",b,"=" ,a//b)
    print("Remainder = ",a%b)

else:
    print("Invalid Operator")