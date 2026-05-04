def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(x):
    if len(x) <2 or len(x) > 6:
        return False
    if not x[0].isalpha() or not x[1].isalpha():
        return False
    if not x.isalnum():
        return False
   # This was the wrong attempt - it will exclude cases where 0 zero comes later on which are totally valid cases
   # for y in x[2:]:
   #     if y =="0":
   #         return False
    for y in range(len(x)):
        if x[y].isdigit():
            if x[y] == "0":
                return False
            if not x[y:].isdigit():
                return False
            
            break

    return True


main()
