import sys
from pyfiglet import Figlet

figlet = Figlet()

def main():
    
    if len(sys.argv) == 1:
        text = input("Input: ").strip()
        if not text:
            sys.exit("Input cannot be empty")
        print("Output:")
        print(figlet.renderText(text))
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in figlet.getFonts():
            sys.exit("You did not input the correct font")
        else:
            figlet.setFont(font = sys.argv[2])
            text = input("Input: ").strip()
            if not text:
                sys.exit("Input cannot be empty")
            print("Output:")
            print(figlet.renderText(text))
    else:
        sys.exit("You did not enter the correct number/type of input")



if __name__ == "__main__":
    main()