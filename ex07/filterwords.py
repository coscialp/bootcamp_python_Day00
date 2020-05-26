import sys
import string


def main():
    if len(sys.argv) != 3:
        print("ERROR")
        return
    try:
        size_max = int(sys.argv[2])
        input_string = sys.argv[1]
        input_string = input_string.translate(str.maketrans('', '', string.punctuation))
        list_args = input_string.split(' ')
        list_ret = []
        for word in list_args:
            if len(word) > size_max:
                list_ret.append(word)
        print(list_ret)
    except ValueError:
        print("ERROR")


if __name__:
    main()