#
# It includes handling for ZeroDivisionError and ValueError.
# This code demonstrates exception handling in Python using try and except
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# This code demonstrates exception handling in Python using try, except, and finally blocks.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

finally:
    print("Execution completed. Thank you for using the program.")



# This code demonstrates exception handling in Python using a function that divides two numbers.# and finally blocks.
# It includes handling for ZeroDivisionError and ValueError.# and finally blocks.
def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")

    finally:
        print("Division operation completed.")

divide_numbers()




try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"The result is: {result}")
    if num ==0:
        raise ZeroDivisionError("You cannot divide by zero.")
    
finally:
    print("Execution completed. Thank you for using the program.")