def main():
    plate = input("Plate: ")
    print(is_valid(plate))



def is_valid(plate):
    plate = plate.strip()
    if not plate:
        return "Invalid"
    if len(plate) > 6 or len(plate)< 2:
        return "Invalid"
    if not plate.isalnum():
        return "Invalid"
    if not plate[0:2].isalpha():
        return "Invalid"
    for x in range(len(plate)):
        if plate[x].isdigit():
            if plate[x]=="0":
                return "Invalid"
            if not plate[x:].isdigit():
                return "Invalid"
            break

    return "Valid"

if __name__ == "__main__":
    main()