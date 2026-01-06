
frontend_students = {"Anu", "Rahul", "Meena", "Kiran"}
backend_students = {"Rahul", "Kiran", "Suresh"}

print("Initial Frontend Students:", frontend_students)
print("Initial Backend Students:", backend_students)

backend_students.add("Priya")

print("\nAfter adding a student to Backend:")
print("Backend Students:", backend_students)
e
frontend_students.remove("Meena")

print("\nAfter removing a student from Frontend:")
print("Frontend Students:", frontend_students)

both_courses = frontend_students & backend_students
print("\nStudents enrolled in BOTH Frontend and Backend:")
print(both_courses)

only_backend = backend_students - frontend_students
print("\nStudents enrolled ONLY in Backend:",only_backend)
all_students = frontend_students | backend_students

print("\nTotal number of unique students:")
print(len(all_students))
course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

print("\nCourse-wise student count:")
print(course_counts)

print("\nCourse details:")
for course, count in course_counts.items():
    print(course, ":", count)

new_course_counts = {
    course: count for course, count in course_counts.items()
}

new_course_counts["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]

print("\nUpdated course dictionary with Fullstack:")
print(new_course_counts)
