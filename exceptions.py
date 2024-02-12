try:
    print(x)
except:
    print("NameError occurred")
finally:
    print("Success")

try:
    num1 = 20
    num2 = 10
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")


# User-defined function
try:
    def sum(first, second):
        return first + second
except:
    print("Something went wrong")
finally:
    print("Success")


print(sum(10, 20))
