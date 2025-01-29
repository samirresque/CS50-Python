from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    f = random.choice(fonts)


    if len(sys.argv) == 1:
        by_random = True


    elif len(sys.argv) == 3 and (sys.argv[1] == "-f") and (sys.argv[2] in fonts):
         by_random = False

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    if by_random == True:  # means that the user gives no other input into command line
        print("Output: \n")
        figlet.setFont(font=f)
        print(figlet.renderText(text))

    else:
        figlet.setFont(font=sys.argv[2])
        print("Output: \n")
        print(figlet.renderText(text))


if __name__ == "__main__":
    main()
