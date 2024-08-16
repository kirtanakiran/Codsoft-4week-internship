
def add(n1, n2):
    result = n1 + n2
    print("{0} + {1} = {2}".format(n1, n2, result))

def sub(n1, n2):
    result = n1 - n2
    print("{0} - {1} = {2}".format(n1, n2, result))

def mul(n1, n2):
    result = n1 * n2
    print("{0} * {1} = {2}".format(n1, n2, result))

def div(n1, n2):
    if n2 == 0.0:
        print("Cannot divide by zero")
    else:
        result = n1 / n2
        print("{0} / {1} = {2}".format(n1, n2, result))

while True:
    print("Operation to be performed:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")  # Option to exit the loop

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting the program.")
        break  # Exit the loop

    n1 = float(input("Enter the number 1: "))
    n2 = float(input("Enter the number 2: "))

    if choice == '1':
        add(n1, n2)
    elif choice == '2':
        sub(n1, n2)
    elif choice == '3':
        mul(n1, n2)
    elif choice == '4':
        div(n1, n2)
    else:
        print("Enter a valid choice")

    
    