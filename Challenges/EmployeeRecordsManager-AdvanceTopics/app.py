# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Challenge: Employee Records Manager
#
# Build a Python program that stores employee records in a JSON file named employees.json.
#
# Requirements
#     1. Add an employee: Ask for their name, salary, and experience. Store each employee as a dictionary.
#     2. Save records: Save the list of employees to employees.json using json.dump().
#     3. Load records: When the program starts, load existing records using json.load(). If the file doesn't exist, start with an empty list.
#     4. Display employees: Print all employee details in a readable format.
#     5. Calculate statistics: Display the average salary and the number of employees with at least 10 years of experience.
#     6. Handle errors: Handle a missing file and invalid numeric input without crashing.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import json
from pathlib import Path


def accept_number_of_employee():
    number_of_employees = get_valid_number(
        "\nHow many employees in your company: ")
    return number_of_employees


def accept_and_return_employee_details(number_of_employees):

    employee_list = []
    for count in range(number_of_employees):
        print(f"\nEnter details for employee {count+1}")

        employee_name = get_valid_name()
        annual_salary = get_valid_input("Enter your anuual salary: ")
        experience = get_valid_input("Enter your experience: ")

        employee = {
            "name": employee_name,
            "salary": annual_salary,
            "experience": experience
        }

        employee_list.append(employee)

    return employee_list


def get_valid_number(prompt_message):
    while True:
        try:
            value = int(input(prompt_message))

            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue

            return value

        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")


def get_valid_name():

    while True:

        name = input("Enter your name: ").strip()

        if not name:
            print("\nName can't be empty. Please enter a proper name.")
            continue

        return name.strip()


def get_valid_input(prompt_message):
    while True:
        try:
            value = float(input(prompt_message))

            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print(
                "\nInvalid input. Please enter numeric values for salary and experience.")


def save_employee_record_into_json(employee_records):
    script_dir = Path(__file__).parent
    file_path = script_dir / "employees.json"

    try:
        with open(file_path, "w") as file:
            json.dump(employee_records, file, indent=4)
    except FileNotFoundError:
        return


def get_employee_record_from_json():
    script_dir = Path(__file__).parent
    file_path = script_dir / "employees.json"

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


# 1. Load existing employee records
employee_records = get_employee_record_from_json()

# 2. Collect new employee records
number_of_employees = accept_number_of_employee()
new_employee_records = accept_and_return_employee_details(number_of_employees)

# 3. Append new employees to existing records
employee_records.extend(new_employee_records)

# 4. Save the combined records
save_employee_record_into_json(employee_records)

# 5. Display all employee records
print("\nAll Employee Details:")

for employee in employee_records:
    print(f"Name: {employee['name']}")
    print(f"Salary: {employee['salary']}")
    print(f"Experience: {employee['experience']}\n")
