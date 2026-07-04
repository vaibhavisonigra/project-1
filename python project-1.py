print(" welcome to the fundamental booster project")

print("fundamental booster")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("exit")

choice = input("enter your choice: ")

a = int(input("enter first number: "))
b = int(input("enter second number: "))

if choice == '1':
    print("addition of two numbers is: ", a + b)
elif choice == '2':
    print("subtraction of two numbers is: ", a - b)
elif choice == '3':
    print("multiplication of two numbers is: ", a * b)
elif choice == '4':
    if b != 0:
        print("division of two numbers is: ", a / b)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == 'exit':
    print("Exiting the program.")
else:
    print("Invalid choice. Please select a valid option.")
    