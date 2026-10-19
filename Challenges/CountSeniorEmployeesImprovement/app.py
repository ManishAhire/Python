# Function to accept employee details
def accept_and_return_employee_details():

    employee_list = []
    for count in range(3):
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
