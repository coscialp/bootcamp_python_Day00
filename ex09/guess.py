from random import randint


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!")

    magic_number = int(randint(1, 99))
    i = 1
    while True:
        print("What's your guess between 1 and 99?\n>> ", end='')
        answer = input()
        if answer == 'exit':
            print("Goodbye")
            return
        answer = int(answer)
        if answer == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("Congratulations! You got it on your first try!")
            return
        elif answer < magic_number:
            print("Too low!")
        elif answer > magic_number:
            print("Too high!")
        elif answer == magic_number:
            print("Congratulations, you've got it !\n You won in {} attempts".format(i))
            return
        i += 1


if __name__:
    main()

