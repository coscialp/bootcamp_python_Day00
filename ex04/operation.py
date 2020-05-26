import sys


def main():
    if len(sys.argv) > 3:
        print("InputError: Too many arguments\n")

    if len(sys.argv) != 3:
        print("Usage: python operation.py <number1> <number2>")
        print("Example:\n\tpython operation.py 10 3")
        return

    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        print("Sum:\t\t\t" + str(a + b))
        print("Difference:\t\t" + str(a - b))
        try:
            div = a / b
            print("Quotient:\t\t" + str(div))
        except ZeroDivisionError:
            print("Quotient:\t\tERROR (div by zero)")

        try:
            mod = a % b
            print("Remainder:\t\t" + str(mod))
        except ZeroDivisionError:
            print("Remainder:\t\tERROR (modulo by zero)")

    except ValueError:
        print("InputError: Only numbers\n")
        print("Usage: python operation.py <number1> <number2>")
        print("Example:\n\tpython operation.py 10 3")


if __name__:
    main()
