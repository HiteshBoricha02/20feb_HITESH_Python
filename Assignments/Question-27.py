# What relationship is appropriate for Course and Faculty?


class Faculty:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, title, faculty):
        self.title = title
        self.faculty = faculty  

# Create a faculty 
faculty = input("Enter The faculty Name :")
faculty2 = input("Enter The second Faculty Name :") 
# create Course

course3 = input("Enter Your Course one :")
course4 = input("Enter Your Course")


faculty1 = Faculty(faculty)

# Create courses and associate them with the faculty member
course1 = Course(course3, faculty1)
course2 = Course(course4, faculty2)

print(f"Course: {course1.title}, Faculty: {course1.faculty.name}")
print(f"Course: {course2.title}, Faculty: {course2.faculty.name}")
