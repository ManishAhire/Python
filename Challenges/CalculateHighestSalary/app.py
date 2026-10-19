# Challenge: Find the highest-paid employee.
# Extend your existing program to:
#     1. Find the employee with the highest current salary.
#     2. Display their name and salary.
#     3. Display the number of employees whose experience is at least 10 years.
# Rules:
#     - Use your existing employee_list.
#     - Create a new function called get_highest_paid_employee(employee_list).
#     - Try solving it with a for loop and an if condition.
#     - Don't use Python's built-in max() yet — I want you to understand the logic first.

# Function to accept employee details
def accept_and_return_employee_details():

    employee_list = []
    for count in range(3):
        print(f"\nEnter details for employee {count+1}")

        try:
            employee_name = input("Enter your name: ")
            annual_salary = float(input("Enter your anuual salary: "))
            experience = float(input("Enter your experience: "))

            employee = {
                "name": employee_name,
                "salary": annual_salary,
                "experience": experience
            }

            employee_list.append(employee)

        except ValueError:
            print("\ncould not convert enter details in to expected type")
            break

    return employee_list


# def get_highest_current_salary(employee_list):

#     if len(employee_list) <= 0:
#         return

#     highest_salary = employee_list[0]["salary"]

#     for employee in employee_list:

#         if employee["salary"] > highest_salary:
#             highest_salary = employee["salary"]

#     return highest_salary

def get_highest_paid_employee(employee_list):

    if not employee_list:
        return None

    highest_paid_employee = employee_list[0]

    for employee in employee_list:

        if employee["salary"] > highest_paid_employee["salary"]:
            highest_paid_employee = employee

    return highest_paid_employee


employee_list = accept_and_return_employee_details()

highest_paid_employee = get_highest_paid_employee(employee_list)

if highest_paid_employee is not None:

    print(f"\nHighest-paid employee: {highest_paid_employee['name']}")
    print(f"Current salary: {highest_paid_employee['salary']:.2f}")


# if len(employee_list) > 0:
#     highest_current_salary = get_highest_current_salary(employee_list)

#     for employee in employee_list:
#         if highest_current_salary == employee["salary"]:
#             print(
#                 f"\nHighest Current Salary of {employee["name"]} is {highest_current_salary}")
