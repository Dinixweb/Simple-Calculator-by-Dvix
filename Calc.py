# Copyright 2018 -- Dennis S (Dvix Concept)
# for educational purposes only
#
# Calculator -- a four function calculator commandline tool
#
# you can add other operator


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


num1 = None
op = None
num2 = None

while (True):

    num1 = float(input("Enter the first value: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the second value: "))
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Invalid number value...")
        op = None

    if (op != None):
        if (op == "+"):
            print("Sum: ", add(num1, num2))
        elif (op == "-"):
            print("Difference: ", sub(num1, num2))
        elif (op == "*"):
            print("Product: ", mult(num1, num2))
        elif (op == "/"):
            print("Quotient: ", div(num1, num2))
        else:
            print("Invalid operator...")

    q = input("Do you want to Exit? [yes/n0] ")
    if (q == "yes" or q == "Yes"):
        break

# -------------------by Dennis (Dvix)------------------------------------ #
