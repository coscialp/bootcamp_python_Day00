import sys


def main():
    languages = {
                    'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '. .-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '0': '-----',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    ' ': ' ',
                }
    if len(sys.argv) < 2:
        print("ERROR")
        return
    chain = ""
    for i in range(1, len(sys.argv)):
        for c in sys.argv[i]:
            c = c.upper()
            try:
                chain += languages[c]
                chain += ' '
            except KeyError:
                print("ERROR")
                return

    print(chain)


if __name__:
    main()
