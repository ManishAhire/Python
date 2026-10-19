
# Create a class
class Bike:
    bike_name = ""
    gare = 0
    company_name = ""

    def get_bike_details(self):
        return f"\nBike Name: {self.bike_name}\nGares: {self.gare}\nCompany Name: {self.company_name}"


# Create a object
bike1 = Bike()

bike1.bike_name = "FZ"
bike1.gare = 5

print(f"\nBike name: {bike1.bike_name} Gare: {bike1.gare}.\n")

bike_details = bike1.get_bike_details()
print("Bike Details are : " + bike_details)

########################################


class Employee:
    def __init__(self, employee_name, age, technology):
        self.employee_name = employee_name
        self.age = age
        self.technology = technology

    def get_employee_details(self):
        return (
            f"\n\nEmployee Name: {self.employee_name}, "
            f"Employee Age: {self.age}, "
            f"Employee Techonology: {self.technology}."
        )


employee1 = Employee("Manish", 27, "Python")

employee_details = employee1.get_employee_details()
print(employee_details)
