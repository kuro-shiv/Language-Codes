## Inheritance using super() function in Python
print("---------------------------------------------------------------")
print("\n")
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary


    def display(self):
        print(f"Name: {self.name }")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)  # Call the parent class constructor
        self.department = department

    def display(self):
        super().display()  # Call the parent class display method
        print(f"Department: {self.department}")

#creating an object of manager 
manager = Manager("Shivam", "M001", 75000, "Web Development")

# Displaying the manager's details
manager.display()

print("\n")  
print("----------------------------------------------------")
print("----------------------------------------------------")
print("\n")  
#class director, teacher and student, student inherits from teacher and teacher inherits from director and student can directly inherit from  # director using super() function
class Director:
    def __init__(self, Director_name, Director_id):
        self.name = Director_name
        self.Id = Director_id

    def display(self):
        print(f"Director Name: {self.name}")
        print(f"Director ID: {self.Id}")

class Teacher(Director):
    def __init__(self,Director_name,Director_Id,Teacher_name,Teacher_id, Teacher_Department):
        super().__init__(Director_name,Director_Id)
        self.name= Teacher_name
        self.Id =Teacher_id
        self.department =Teacher_Department

    def display(self):
        super().display()
        print(f"Teacher Name: {self.name}")
        print(f"Teacher ID: {self.Id}")
        print(f"Teacher Department: {self.department}")


class student(Teacher):
    def __init__(self, Director_name, Director_Id, Teacher_name, Teacher_id, Teacher_Department, Student_name, Student_id):
        super().__init__(Director_name, Director_Id, Teacher_name, Teacher_id, Teacher_Department)
        self.name = Student_name
        self.Id = Student_id

    def display(self):
        super().display()
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.Id}")

# Creating an object of student
student_obj = student("Candy", "LUN1", "Ruby", "Tea01", "Web Development", "Shivam"," stud01")

# Displaying the student's details
student_obj.display()


print("\n")  # Print a newline for better readability
print("----------------------------------------------------")

