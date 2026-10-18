student_id = {1, 2, 3, 4, 5, 2, 3, 1, 6}
print("Student IDs: ", student_id)

mix_set = {"ABC", True, 1234}
print(f"Mix Data Types: {mix_set}")

student_id.add(123)
print(student_id)

languages = {"C", "C++", "Java", "Swift", "Python"}
languages.discard("Swift")
print(languages)

for item in languages:
    print(item)

print("Total lenght: ", len(languages))
