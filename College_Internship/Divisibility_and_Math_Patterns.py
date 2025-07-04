#Print all numbers divisible by 3 and 5 between 1 to N
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
        print("\n")


#Print squares of numbers from 1 to N
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(i ** 2, end=' ')
    print("\n")

#Print a pattern of stars *

#triangle pattern
N = int(input("Enter the number of rows for the triangle pattern: "))
for i in range(1, N + 1):
    print('*' * i)
    print("\n")

# inverted triangle pattern
N = int(input("Enter the number of rows for the inverted triangle pattern: "))  
for i in range(N, 0, -1):
    print('*' * i)
    print("\n")

# diamond pattern
N = int(input("Enter the number of rows for the diamond pattern: "))
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
    print("\n")
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
    print("\n")

# hollow square pattern
N = int(input("Enter the size of the hollow square pattern: "))
for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print("\n")

    