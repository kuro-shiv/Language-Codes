#define a class
class Bike:
    name = " "
    gear= 0

objbikel = Bike()

#accwss attribute and assign new value
objbikel.name = "Mountain Bike"
objbikel.gear = 5


print(f"Name: {objbikel.name}, Gear: {objbikel.gear}")


#Define a class Employee
class Employee:

    Employee_id = 0
    Employee_name = " "
    Employee_salary = 0.0

Employee1 = Employee()
Employee2 = Employee()

#Access properties using employee1
Employee1.Employee_id = 101
Employee1.Employee_name = "Shivam Kumar Dubey"  
Employee1.Employee_salary = 500000.0
print(f"Employee ID: {Employee1.Employee_id}, Name: {Employee1.Employee_name}, Salary: {Employee1.Employee_salary}")

#Access properties using employee2
Employee2.Employee_id = 102
Employee2.Employee_name = "Aditi Pandey"
Employee2.Employee_salary = 60000.0
print(f"Employee ID: {Employee2.Employee_id}, Name: {Employee2.Employee_name}, Salary: {Employee2.Employee_salary}")


#create a class called area operations
class AreaOperations:
    length = 0.0
    width = 0.0
    side = 0.0

    #define a method to calculate area of rectangle
    def area_of_rectangle(self):                               #self refers to the instance of the class
        rec_area = self.length * self.width
        print("Area of rectangle = ",self.length * self.width)
        print(f"Area of Rectangle: {rec_area}")
        return rec_area
    #define a method to calculate area of square
    def area_of_square(self):
        sq_area = self.side * self.side
        print("Area of rectangle = ",self.side * self.side)
        print(f"Area of Square: {sq_area}")
        return sq_area
    
#create an object of area operations class
area_of_rectangle_object = AreaOperations()
area_of_square_object = AreaOperations()

#assign values to the attributes
area_of_rectangle_object.length = 10.0
area_of_rectangle_object.width = 5.0

area_of_square_object.side = 4.0

#call the methods to calculate area
area_of_rectangle_object.area_of_rectangle()
area_of_square_object.area_of_square()



#class for arthmetic operations
class ArithmeticOperations:
    num1 = 0.0 
    num2 = 0.0 

    #user input for numbers
    def get_numbers(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def add(self):
        result = self.num1 + self.num2
        return result
    
    def subtract(self):
        result = self.num1 - self.num2
        return result
    
    def multiply(self):
        result = self.num1 * self.num2
        return result
    
    def divide(self):
        result = self.num1 / self.num2
        return result
    
# Create an object of ArithmeticOperations class
arithmetic_operations_object = ArithmeticOperations()
# Get numbers from user
arithmetic_operations_object.get_numbers()
# Perform arithmetic operations
addition_result = arithmetic_operations_object.add()
subtraction_result = arithmetic_operations_object.subtract()
multiplication_result = arithmetic_operations_object.multiply()
division_result = arithmetic_operations_object.divide()
# Print the results
print(f"Addition: {addition_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")

