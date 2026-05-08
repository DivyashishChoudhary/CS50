import random

def main():
    while True:
        try:
            max_value = int(input("Level: "))
            if max_value <= 0:
                continue
            break
        except ValueError:
            continue
            
    random_number = random.randint(1,max_value)
    
    while True:
        try:
            guess_value = int(input("Guess: "))
            if guess_value <= 0:
                continue
            if guess_value == random_number:
                print("Just right!")
                break
            elif guess_value < random_number:
                print("Too small!")
            else:
                print("Too large!")

        except ValueError:
            continue











if __name__ == "__main__":
    main()