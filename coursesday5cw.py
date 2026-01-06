python_students={"Anu","Rahul","Abhin"}
data_science_students={"Rahul","Monica","Sangeetha"}

python_students.add("Lilly")
data_science_students.remove("Monica")

print("Students enrolled in both the courses:",python_students&data_science_students)

print("Students enrolled in Python and not in Data Science:",python_students-data_science_students)

print("List of students in either courses:",python_students|data_science_students)

course={"python":len(python_students),
        "data_science":len(data_science_students)}
my_course=dict(course)
print(my_course)

