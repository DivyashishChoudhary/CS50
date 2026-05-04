def main():
    prompt = input("Input text: ")
    output = []
    for letter in prompt:
        if letter in {"a","e","i","o","u","A","E","I","O","U"}:
            pass  
        
        else:
            output.append(letter)

    output = "".join(output)
    print(output)
    

        



if __name__ == "__main__":
    main()