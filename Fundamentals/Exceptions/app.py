
# divide_number = 7 / 0
# print("Divide Number by 0: ", divide_number) # ZeroDivisionError: division by zero

########### try except ##########
try:
    divide_number = 7 / 0
    print("Divide Number by 0: ", divide_number)

except:
    print("\nCan't perform 7 / 0")


########### Handler specific exception ##########

# even_numbers = [2, 4, 6, 8]
# print("Even number: ", even_numbers[5]) # IndexError Exception


try:
    even_numbers = [2, 4, 6, 8]
    print("\nEven number: ", even_numbers[5])

    divide_number = 7 / 0
    print("\nDivide Number by 0: ", divide_number)

except IndexError:
    print("\nIndex Out of Bound.")

except ZeroDivisionError:
    print("\nDenominator cannot be 0.")

except:
    print("\nError")


########### try with else ##########

try:
    even_numbers = [2, 4, 6, 8]
    print("\nEven number: ", even_numbers[1])

except:
    print("\nIndex Out of Bound.")

else:
    print("Yes.. It's a even number. That's correct. \n")


########### try with finally ##########
try:
    even_numbers = [2, 4, 6, 8]
    print("\nEven number: ", even_numbers[8])

except:
    print("\nIndex Out of Bound.")

finally:
    print("Finally block - alway excecute.\n")


########### custome exception ##########

class InvalideAgeException(Exception):
    pass


number = 18

try:
    input_number = int(input("Enter your age: "))

    if input_number < number:
        raise InvalideAgeException
    else:
        print("You're eligiable for vote.\n")

except InvalideAgeException:
    print("InvalideAgeException Occurred - Invalid age\n")


# List of all built in exceptions - ZeroDivisionError, MemoryError, ImportError ect
# print(dir(locals()['__builtins__']))
