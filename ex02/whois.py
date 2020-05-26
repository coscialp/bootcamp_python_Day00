import sys


def main():
    if len(sys.argv) > 2:
        print("ERROR")
        return
    try:
        nb = int(sys.argv[1])

        if nb == 0:
            print("I\'m Zero")
        elif nb % 2:
            print("I\'m Odd")
        else:
            print("I'm Even")

    except ValueError:
        print("ERROR")
    except IndexError:
        print("ERROR")


if __name__:
    main()
