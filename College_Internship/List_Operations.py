#Find maximum number in a list
def find_maximum(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Find minimum number in a list
def find_minimum(numbers):  
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

#Print elements of a list
def print_elements(numbers):
    if not numbers:
        print("The list is empty.")
        return
    for num in numbers:
        print(num, end=' ')
    print("\n") 

#Take N inputs from user and print them
def take_inputs_and_print(N):
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    print("You entered:", end=' ')
    print_elements(numbers)

#Calculate average of N numbers
def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

#calling all functions
if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 4]
    
    print("Maximum number:", find_maximum(numbers))
    print("Minimum number:", find_minimum(numbers))
    
    print("Elements in the list:")
    print_elements(numbers)
    
    N = int(input("How many numbers do you want to input? "))
    take_inputs_and_print(N)
    
    average = calculate_average(numbers)
    if average is not None:
        print("Average of the numbers:", average)
    else:
        print("No numbers to calculate average.")