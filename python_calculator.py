calculate = "Y"


while calculate == "Y" or calculate == "y":
    first_number_string = input("Number 1: ")
    second_number_string = input("Number 2: ")
    first_number = float(first_number_string)
    second_number = float(second_number_string)
    operator = input("Choose: +, -, * or /")
    print(first_number, second_number)
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    else:
        print("invalid operator...")
    
    calculate = input("Type 'Y' to make another calculation: ")

print("End of program")