N = int(input("Enter a number: "))

#print number from 1 to N
for i in range(1, N + 1):
    print(i, end=' ')
    print("\n")


# Print even numbers from 1 to N
for i in range(1, N + 1):
    if i % 2 == 0:
       print(i, end=' ')   
       print("\n")


# Print odd numbers from 1 to N
for i in range(1, N + 1,2):
    print(i, end=' ')
    print("\n")


# Print sum of numbers from 1 to N
sum = 0
for i in range(1, N + 1):
    sum += i
print("Sum of numbers from 1 to", N, "is:", sum)
print("\n") 

# Print multiplication table of a number
for i in range(1, 11):
    print(N, "x", i, "=", N * i)    
print("\n") 


# Print factorial of a number
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print("Factorial of", N, "is:", factorial)
print("\n")


