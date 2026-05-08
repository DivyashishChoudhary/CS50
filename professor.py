import random

def main():
    score = 0
    level = get_level()
    
    
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        wrong_counter = 0
        while True:
            try:
                if wrong_counter >=3:
                    print(f"{x} + {y} = {answer}")
                    break
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    wrong_counter += 1
                
            except ValueError:
                print("EEE")
                wrong_counter +=1
    
    print(f"Score: {score}")
    
    
    

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level not in [1,2,3]:
                continue
            else:
                return level
        except ValueError:
            continue




def generate_integer(level):
    
    if level==1:
        return random.randint(0,9)
    if level==2:
        return random.randint(10,99)
    if level==3:
        return random.randint(100,999)
    raise ValueError("Level must be 1,2 or 3")

    
'''
    int_1 = random.randint(1,9)
    if level ==1:
        return "".join(int_1)
    
    if level ==2:
        int_2 = random.randint(0,9)
        return "".join([str(int_1),str(int_2)])
    
    if level ==3:
        int_2 = random.randint(0,9)
        int_3 = random.randint(0,9)
        return "".join([str(int_1),str(int_2), str(int_3)])
'''





if __name__ == "__main__":
    main()