temperature = 34
if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that determines the largest number among three numbers
num1 = 50
num2 = 89
num3 = 21
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 89
if number % 2 == 0:
    print(number, "is even")
else:
    print(number,"is odd")

# A program that checks whether a number is a prime number
number = int(input("Enter number"))
if number == 1:
    print(number, "is not a prime number")
elif number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            print(i, "times", number // i, "is", number)
            break
    else:
        print(number, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(number, "is not a prime number")
