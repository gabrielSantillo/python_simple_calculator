def add_function():
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    except:
        print("Something went wrong. Ask for help.")

    result = num_one + num_two
    print("Your result is: ", result, "\n")

def sub_function():
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    except:
        print("Something went wrong. Ask for help.")

    result = num_one - num_two
    print("Your result is: ", result,"\n")

def multi_function():
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    except:
        print("Something went wrong. Ask for help.")

    result = num_one * num_two
    print("Your result is: ", result,"\n")

def divi_function():
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    except:
        print("Something went wrong. Ask for help.")
    try:
        result = num_one / num_two
    except ZeroDivisionError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return

    print("Your result is: ", result,"\n")


def input_selection():
    print("\nWelcome to the simple calculator, please select from the following options:\n")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    try:
        selection = float(input("\nPlease enter your selection: "))
    except ValueError:
        print("Please, enter only numbers.")
        selection = input_selection()
    except:
        print("Something went wrong. Ask for help.")

    if (selection == 1.0):
        add_function()
        use_again = input("\nWanna use the calculator again? y/n\n")
    elif(selection == 2.0):
        sub_function()
        use_again = input("\nWanna use the calculator again? y/n\n")
    elif(selection == 3.0):
        multi_function()
        use_again = input("\nWanna use the calculator again? y/n\n")
    elif(selection == 4.0):
        divi_function()
        use_again = input("\nWanna use the calculator again? y/n\n")
    else:
        print("Please, enter a number between 1 to 4.\n")
        input_selection()

    if(use_again == "y" or use_again == "Y"):
        answer = "y"
    elif(use_again == "n" or use_again == "Y"):
        print("Thank you for using my calculator.")
        answer = "n"
    
    return answer

while True:
    input_selection()
    if input_selection() == "n":
        break
