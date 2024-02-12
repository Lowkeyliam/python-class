# Data Type
number = 67  # int
num = 78.98  # float
greeting = "Hello there"  # str
IsPythonInteresting = True  # bool

# A variable storing multiple values
languages = ["Python", "Java", "PHP"]  # list
fruits = ("apple", "banana", "pinapple")  # tuple
countries = {"Kenya", "North America", "China"}  # set
# Dictionary
details = {
    "firstname": "Liam",
    "age": 18,
    "course": "MIT",
    "nationality": "France",
}
print(number)
print(IsPythonInteresting)
print(countries)
print(details)
print(details["course"])

# Determining the data type
print(type(details))
print(type(countries))
print(type(fruits))

# Typecasting - converting one data type to another
print(float(number))
print(int(num))
