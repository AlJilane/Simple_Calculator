def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ("+", "-", "*", "/"):
            return operation
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

def perform_operation(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero. Please enter a non-zero number.")
            return None
        return first_number / second_number

def ask_repeat():
    while True:
        repeat = input("Do you want to perform another operation (y/n): ").lower()
        if repeat in ('y', 'n'):
            return repeat
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    while True:
        first_number = get_number("Enter first number: ")
        operation = get_operation()
        second_number = get_number("Enter second number: ")

        result = perform_operation(first_number, second_number, operation)
        if result is not None:
            print("Result is:", result)

        repeat = ask_repeat()
        if repeat == "n":
            break

    print("Program exited")

if __name__ == "__main__":
    main()
