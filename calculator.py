x = int(input("Enter first value :"))
y = int(input("Enter second value :"))
op = input("enter an operator :")
if op == "+":
    print("The sum of", x, "and", y, "is", x + y)
elif op == "*":
    print("The product of", x, "and", y, "is", x * y)
elif op == "-":
    print("The difference of", x, "and", y, "is", x - y)
elif op == "/":
    print("The quotient of", x, "and", y, "is", x / y)
else:
    print("Invalid operator entered")