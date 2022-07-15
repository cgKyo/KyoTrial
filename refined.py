def num_input(
    first_input_text = "Enter your first number",
    second_input_text = "Enter your second number"
):
    num1 = int(input(f"{first_input_text}: "))
    num2 = int(input(f"{second_input_text}: "))
    return num1, num2 

def list_operations_list():
    var_operations_list = ["Addition", "Subtraction", "Multiplication", "Division"]
    for index, operation in enumerate(var_operations_list, start=1):
        print(f"({index})", operation)

def main():
    print("Welcome to KYOS BIG DICK CALCULATOR BABY. What you trying to solve baby gurl?")

    var_operations_dict = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Division",
        "5": "Modulus",
    }

    for key, value in var_operations_dict.items():
        print(f"({key})", value)

    num = (input())

    if var_operations_dict[num] == "Addition":
        num1, num2 = num_input()
        sum = num1 + num2
        print("The Sum Is ", sum)
    elif var_operations_dict[num] == "Subtraction":
        num1, num2 = num_input()
        sum = num1 - num2
        print("The Difference Is ", sum)
    elif var_operations_dict[num] == "Multiplication":
        num1, num2 = num_input()
        sum = num1 * num2
        print("The Product Is ", sum)
    elif var_operations_dict[num] == "Division":
        num1, num2 = num_input()
        sum = num1 / num2
        print("The Quotient Is ", sum)
    elif var_operations_dict[num] == "Modulus":
        num1, num2 = num_input()
        sum = num1 % num2
        print("The Modulus Is ", sum)
    else:
        print("Thats not a number in the list you silly billy goose.")

if __name__ == "__main__":
    main()

    # print(test_dict.get("keythatisntreal", "default_value"))

    # # simple for loop
    # for operation in var_operations_list:
    #     print(operation)
    
    # # for loop with an index
    # for index, operation in enumerate(var_operations_list, start=1):
    #     print(index, operation)
    
    # # string in string
    # if "fart" in "superfartingcows":
    #     print("found fart")

    # # is the operation in the operations list
    # if "Addition" in var_operations_list:
    #     print("Addition is supported")
