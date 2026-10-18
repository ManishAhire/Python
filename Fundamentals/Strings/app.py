first = "Manish"
last = "Ahire"
fullName = first + " " + last
print(fullName)

formated_string1 = f"{first} {last}"
print(formated_string1)

validExpression = f"{len(first)} {2 + 3}"
print(validExpression)

# String Methods
course = "     python programming  "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.find("G"))
print(course.replace("p", "*"))
print("pro" in course)
print("swift" not in course)
