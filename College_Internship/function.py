#This script defines a function that prints a greeting message
def greet():
    print("Hello, World!")

greet()

print("This is a function that prints a greeting message.")


#function with 2 parameters 

def area_of_rectangle():
    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")
    length = float(length)
    width = float(width)
    # Calculate the area of the rectangle
    result = length * width
    print(f"The area of the rectangle is: {result}")
    return result

area_of_rectangle()


def area_of_circle(radius):
    radius = float(radius)
    # Calculate the area of the circle
    area = 3.14 * radius * radius
    print(f"The area of the circle is: {area}")
    return area


radius = input("Enter the radius of the circle: ")
Circle = area_of_circle(radius)

# Function to calculate the area of a triangle with parameters for base and height
def area_of_triangle(base, height):
    base = input("Enter the base of the triangle: ")
    height = input("Enter the height of the triangle: ")
    base = float(base)
    height = float(height)
    # Calculate the area of the triangle
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
    return area


