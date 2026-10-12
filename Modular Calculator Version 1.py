num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return "Can't divide by zero."
    return num1 / num2


print("\nChoose operation:")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

choice = input("\nEnter choice: ")

if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid operation choice."

print("\nResult:", result)
