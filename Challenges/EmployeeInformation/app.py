# Challenge: Employee Information & Salary Analyzer

# Write a Python program that:

# Asks the user for their name.

# Asks for their current salary and years of experience.

# Calculates a hypothetical 10% salary increase.

# Displays the employee's information.

# If experience is 10 years or more, prints Senior Engineer; otherwise, prints Engineer.

# Displays the new salary rounded to two decimal places.

# Example output:

# Enter your name: Manish
# Enter your current annual salary: 1200000
# Enter years of experience: 11

# --- Employee Report ---
# Name: Manish
# Experience: 11 years
# Role: Senior Engineer
# Current Salary: 1200000.00
# Salary After 10% Increase: 1320000.00
# Rules for this challenge

# Use variables, input(), type conversion, if/else and f-strings.

# Don't use AI to generate the complete solution.

# Try it yourself first. If you get stuck, I'll give you hints.


employee_name = input("Enter your name: ")
annual_salary = float(input("Enter your current annual salary: "))
total_experience = float(input("Enter years of experience: "))

if total_experience >= 10:
    role = "Senior Engineer"
else:
    role = "Engineer"

increasedSalary = annual_salary * 1.10

print("\n --- Employee Report ---")
print(f"Name: {employee_name}")
print(f"Experience: {total_experience:g} years")
print(f"Role: {role}")
print(f"Current Salary: {annual_salary:.2f}")
print(f"Salary After 10% Increase: {increasedSalary:.2f}")
