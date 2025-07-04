# Basic Looping and Number Operations

#FOR LOOP EXAMPLES

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



#WHILE LOOP EXAMPLES

#print pattern with 1 and 2 and 3 using while loop, print 3 times the value of i with j and j will go 1 then 2 then 3 and then again 1,2,3
i = 1
while i <= 3:
    j = 1
    while j <= 3:   
        print(i, j)
        j += 1
    i += 1


