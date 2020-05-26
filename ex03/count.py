import string


class Info:

    def __init__(self):
        self.uppercase = 0
        self.lowercase = 0
        self.space = 0
        self.punctuation = 0
        self.character = 0


def ispunct(c):
    for char in string.punctuation:
        if c == char:
            return True
    return False


def text_analyzer(*lines):

    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""

    if len(lines) > 1:
        print("ERROR")
        return

    info = Info()
    try:
        line = lines[0]
    except IndexError:
        print("What is the text to analyse?\n>> ", end='')
        line = input()

    for c in line:
        info.character += 1
        if c.isupper():
            info.uppercase += 1
        elif c.islower():
            info.lowercase += 1
        elif c.isspace():
            info.space += 1
        elif ispunct(c):
            info.punctuation += 1

    text = "The text contains " + str(info.character) + " characters:\n\n- " + str(info.uppercase) + " upper letters\n"
    text += "\n- " + str(info.lowercase) + " lower letters\n\n" + "- " + str(info.punctuation) + " punctuation marks\n"
    text += "\n- " + str(info.space) + " spaces"

    print(text)
