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
            print(
                "\nInvalid input. Please enter numeric values for salary and experience.")
            break

    return employee_list


def get_senior_employee_names(employee_list):
    senior_employee_names = []

    for employee in employee_list:
        if employee["experience"] >= 10:
            senior_employee_names.append(employee["name"])

    return senior_employee_names


employee_list = accept_and_return_employee_details()
senior_employee_names = get_senior_employee_names(employee_list)

print("\nSenior employees:")
for name in senior_employee_names:
    print(name)

print(
    f"\nNumber of employees with 10+ years of experience: {len(senior_employee_names)}.\n")
