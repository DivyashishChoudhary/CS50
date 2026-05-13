import sys

def main():
    if len(sys.argv) !=2:
        sys.exit("Input is not compatible, please input file name only")
    extension = sys.argv[1][-3:]
    if extension != ".py":
        sys.exit("Input is not compatible, please input .py file only")

    line_counter = 0                
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line:
                    if line[0] =="#":
                        continue
                    line_counter +=1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_counter)


if __name__ == "__main__":
    main()