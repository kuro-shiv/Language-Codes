#class of student
class Student:
    def __init__(self, name, age):
        print("Default Constructor called")
    def __init__(self, name, age, grade):
        print("Constructor called with three parameters")
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
# Example usage
student1 = Student("Alice", 20, "A")
print(student1.name, student1.age, student1.grade)




#class of Employee
class Employee:
    def __init__(self, name, age):
        print("Default Constructor called")
        self.name = name
        self.age = age
        return f"Name: {self.name}, Age: {self.age}"

    def __init__(self, Name, ID, Slalary, Country):
        print("Constructor called with four parameters")
        self.Name = Name
        self.ID = ID
        self.Salary = Slalary
        self.Country = Country

    def get_info(self):
        return f"Name: {self.Name}, ID: {self.ID}, Salary: {self.Salary}, Country: {self.Country}"
    
# 2 Example usage
employee1 = Employee("Bob", "E123", 50000, "USA")
print(employee1.Name, employee1.ID, employee1.Salary, employee1.Country, "\n")

employee2 = Employee("Alice", "E456", 60000, "Canada")
print(employee2.Name, employee2.ID, employee2.Salary, employee2.Country)