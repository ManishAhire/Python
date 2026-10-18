
for number in range(3):
    print("Message", number)

print("\n")

for number in range(1, 5):
    print("Message", number)


print("\n")

for number in range(1, 10,  2):
    print("Message", number)


print("\n")

sucess = True
for number in range(5):
    print("Message")

    if sucess:
        print("Sucess")
        break

print("\n")
sucess = False
for number in range(5):
    print("Attempt")

    if sucess:
        print("Sucess")
        break
else:
    print(f"Attempted {number+1} times and failed")

# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# While Loop
number = 5
while number > 0:
    print(number)
    number -= 1
