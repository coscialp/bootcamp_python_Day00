import sys


def main():
    if len(sys.argv) > 1:
        string = sys.argv[1]
    for i in range(2, len(sys.argv)):
        string += " " + sys.argv[i]

    rev = string[::-1]
    print(rev.swapcase())


if __name__:
    main()
