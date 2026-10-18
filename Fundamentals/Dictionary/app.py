employee_details = {
    "Name": "Pradnyesh",
    "Age": 6,
    "isAvailable": True
}

print("\nEmployee Details: ", employee_details)

print("\nEmployee Name: ", employee_details["Name"])

employee_details["Salary"] = 12345.90
print("\nEmployee Details with Salary: ", employee_details)

del employee_details["isAvailable"]
print("\nRemoved isAvailable key: ", employee_details)

employee_details["Salary"] = 2200000
print("\nChange the Salary item: ", employee_details)

print("\nKeys in dict: ")
# For Loop
for key in employee_details:
    print(key)

print("\nKey:Values in dict: ")
for key in employee_details:
    value = employee_details[key]
    print(f"{key}:{value}")


# Clear the dic
employee_details.clear()
print("\nClear the dic: ", employee_details)
