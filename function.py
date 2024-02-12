# Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

num = min(34, 78, 90, 123, 45)
print(num)

z = (2, 3)
print(z)


# User-defined function
def name():
    print("Liam")


name()  # Calling a function


def details():
    myname = "Liam"
    age = 19
    course = "MIT"
    print(myname, age, course)


details()


# Parameters/variables and arguments/values
def patient(name, gender, age, status):
    print(name, gender, age, status)


patient("Liam", "Male", 19, "single")
patient("Kerry", "Female", 18, "single")


def multiply(x, y):
    print(x * y)


multiply(10, 5)
multiply(10, 45)


# Create a user defined function called employees, display details of 5 employees
# fullname, age ,position, salary
def employees(fullname, age, position, salary):
    print(fullname, age, position, salary)


employees("Terry Ann", 20, "manager", "Ksh. 20,000")
employees("James Mwangi", 19, "Janitor", "Ksh. 5,000")
employees("Liam Maina", 19, "CEO", "Ksh. 200,000")
employees("Michael Angelo", 20, "Director", "Ksh. 10,000")
employees("Winnie Pooh", 20, "HR", "Ksh. 100,000")