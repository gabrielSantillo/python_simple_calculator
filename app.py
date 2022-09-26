# this function will do a simple sum math
def add_function():
    # getting 2 numbers of the user and surrounding by the try
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    # if a ValueError error occur, show a message to the user and return the function
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    # if any other error occur show to the user a message
    except:
        print("Something went wrong. Ask for help.")

    # storing the result of the sum math in a variable and printing the result
    result = num_one + num_two
    print("Your result is: ", result, "\n")

# this function will do a simple sub math


def sub_function():
    # getting 2 numbers of the user and surrounding by the try
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    # if a ValueError error occur, show a message to the user and return the function
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    # if any other error occur show to the user a message
    except:
        print("Something went wrong. Ask for help.")
    # storing the result of the sub math in a variable and printing the result
    result = num_one - num_two
    print("Your result is: ", result, "\n")

# this function will do a simple multiplication math
def multi_function():
    # getting 2 numbers of the user and surrounding by the try
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    # if a ValueError error occur, show a message to the user and return the function
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    # if any other error occur show to the user a message
    except:
        print("Something went wrong. Ask for help.")
    # storing the result of the multiplication math in a variable and printing the result
    result = num_one * num_two
    print("Your result is: ", result, "\n")

# this function will do a simple division math
def divi_function():
    # getting 2 numbers of the user and surrounding by the try
    try:
        num_one = float(input("Please enter your first number: "))
        num_two = float(input("Please enter your second number: "))
    # if a ValueError error occur, show a message to the user and return the function
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    # if any other error occur show to the user a message
    except:
        print("Something went wrong. Ask for help.")
    # trying to do the division math
    try:
        result = num_one / num_two
    # catching the error if the second number is zero and returning the function
    except ZeroDivisionError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again\n")
        return
    # printing te result
    print("Your result is: ", result, "\n")

# this function is responsible to ask if the user want to reuse the calculator
def continue_using_calc():
    # asking the user if he wants to continue to use the calculator and storing in a variable
    use_again = input("\nWanna use the calculator again? y/n\n")
    # if the answer is y or Y, return true
    if (use_again == "y" or use_again == "Y"):
        return True
    # if the answer is n or N, return false
    elif (use_again == "n" or use_again == "Y"):
        print("Thank you for using my calculator.")
        return False
    # if the user types any other caracter, print a message to type only the allowed answer and call the function again
    else:
        print("Please, type y for yes or n for no.")
        continue_using_calc()

# this function ask the user what math he wants to do
def input_selection():
    print("\nWelcome to the simple calculator, please select from the following options:\n")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    # trying to storing the answer in a variable
    try:
        selection = float(input("\nPlease enter your selection: "))
    # if the user type anything but numbers, print out a message and call the function again
    except ValueError:
        print("Please, enter only numbers.")
        selection = input_selection()
    # any other exception print a message to call for help
    except:
        print("Something went wrong. Ask for help.")

    # this if statement call a function based on the selection value
    if (selection == 1.0):
        add_function()
    elif (selection == 2.0):
        sub_function()
    elif (selection == 3.0):
        multi_function()
    elif (selection == 4.0):
        divi_function()
    # if the number anything but 1, 2, 3 or 4, print a message and call this function again
    else:
        print("Please, enter a number between 1 to 4.\n")
        input_selection()

    return continue_using_calc()

# storing the user input selection returned in the function input_selection()
use_again = input_selection()

# infinite while loop that call the function while its true
while use_again:
    continue_math = input_selection()
    # if the answer is false, the not will change the value to true and break the loop
    if not continue_math:
        break
