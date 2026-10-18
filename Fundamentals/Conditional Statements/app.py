age = 15
if age >= 18:
    print("You're 18+ :)")
    print("Nice")
elif age <= 5:
    print("You're baby ;)")
else:
    print("Wait still 18")

age = 12
if age >= 18:
    message = "Eligiable"
else:
    message = "Not Eligiable"

print(message)

message = "Eligibale" if age >= 18 else "Not Eligibale"
print(message)

if 18 <= age < 65:
    print("Eligibale")
else:
    print("Not Eligibale")


high_income = True
good_credits = True

if high_income and good_credits:
    print("Eligiable for Loan")
else:
    print("Not Eligiable for Loan")

student = False

if not student:
    print("Student eligiable for loan")
else:
    print("Student not eligiable for loan")

if (high_income or good_credits) and not student:
    print("Eligiable for loan")
else:
    print("Not eligiable for loan")
