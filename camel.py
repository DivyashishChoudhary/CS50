def main():
   dis_val = snake_case_maker(input("camelCase: "))
   print(dis_val)

def snake_case_maker(message):
    dis_val = []
    for letter in message:
        if letter.islower():
            dis_val.append(letter)
        elif letter.isupper():
            dis_val.append("_")
            dis_val.append(letter.lower())
    return "".join(dis_val)


main()


