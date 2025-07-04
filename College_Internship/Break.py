#GET CONDITION FROM USER
intialize = input("Enter the initial value: ")
testing_condition = input("Enter the testing condition: ")
# Convert inputs to integers
intialize = int(intialize)
testing_condition = int(testing_condition)
# Example of using a break statement in a loop dont print break statement and continue the loop
for i in range(intialize, testing_condition + 1):
    if i == 5:  # Example condition to break the loop
        break
    print(i, end=' ')
print("\nLoop ended at:", i)




#continue statement example of current loop
for i in range(intialize, testing_condition + 1):
    if i == 5:  # Example condition to skip the current iteration
        continue
    print(i, end=' ')
print("\nLoop continued after skipping 5")
