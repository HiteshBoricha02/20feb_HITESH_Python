

# What relationship is appropriate for Student and Person?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def display_student_info(self):
        self.display_info()  
        print(f"Student ID: {self.student_id}")


name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
student_id = int(input("Enter Student Id :"))
student = Student(name, age, student_id)


student.display_student_info()
