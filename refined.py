def num_input(first_input_string = "Enter your first number: "):
    num1 = int(input(first_input_string))
    num2 = int(input("Enter your second number: "))
    return num1, num2 



if __name__ == "__main__":
    print("Welcome to KYOS BIG DICK CALCULATOR BABY. What you trying to solve baby gurl?\n 1(Addition) 2(Subtraction) 3(Multiplication) 4(Division)")
    num = (input())

    if num == "1":
        num1, num2 = num_input()
        sum = num1 + num2
        print("The Sum Is ", sum)

        
    if num == "2":
        num1, num2 = num_input()
        sum = num1 - num2
        print("The Difference Is ", sum)

        

    if num == "3":
        num1, num2 = num_input()
        sum = num1 * num2
        print("The Product Is ", sum)

        

    if num == "4":
        num1, num2 = num_input(first_input_string = "Name, enter your number")
        sum = num1 / num2
        print("The Quotient Is ", sum)

    else:
        print("Thats not a number in the list you silly billy goose.")

    

