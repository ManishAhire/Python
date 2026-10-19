
# Function to accept employee details
def accept_and_return_employee_details():

    employee_list = []
    for count in range(3):
        print(f"\nEnter details for employee {count+1}")
        employee_name = input("Enter your name: ")
        annual_salary = float(input("Enter your anuual salary: "))
        experience = float(input("Enter your experience: "))

        employee = {
            "name": employee_name,
            "salary": annual_salary,
            "experience": experience
        }

        employee_list.append(employee)

    return employee_list


# Display employee details
def display_employee_details(employee_list):

    print("\nEmployees Details are: \n")

    for employee in employee_list:
        print(f"Name: {employee["name"]}")

        increasedSalary = employee["salary"] * 1.10
        print(f"Aalary after a 10% increase: {increasedSalary}")

        print(f"Experience: {employee["experience"]}\n")


def get_avarage_salary_for_employees(employee_list):
    total_salary = 0
    for employee in employee_list:
        salary = employee["salary"]
        total_salary += salary

    avarage_salary = total_salary / len(employee_list)
    return avarage_salary


employee_list = accept_and_return_employee_details()
display_employee_details(employee_list)

avarage_salary = get_avarage_salary_for_employees(employee_list)
print("\nAvarage Salary of employees is: ", avarage_salary)
