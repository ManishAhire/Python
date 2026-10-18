def greet(firstName, lastName):
    print(f"Hello {firstName} {lastName}")
    print("Welcome to Python Learning")


greet("Manish", "Ahire")


def addition(a, b):
    return a + b


result = addition(22, 11)
print(f"Addition is: {result}")

# file = open("additionResult.txt", "w")
# file.write(f"Addition is: {result}")


def increment(number, by=1):
    return number + by


result = increment(10, 5)
print(f"Increment result: {result}")


def find_sum(*numbers):
    result = 0

    for number in numbers:
        result += number

    print("Sum: ", result)


find_sum(1, 2, 3)
