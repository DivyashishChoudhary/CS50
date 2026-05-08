def main():
    name_list = []
    while True:
        
        '''
        try:
            name_input = input("Name:").strip()
            name_list.append(name_input)
        
        except EOFError:
            output = name_list[0]
            if len(name_list) ==1:
                print(f"Adieu, adieu, to {name_list[0]}")
                break
            elif len(name_list) ==2:
                print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
                break
            else:
                for name in name_list[1:-1]:   # This operation can be done just once, doesn't have to be done n times join command allows for that sort of usability
                    output = ", ".join([output,name])
                print(f"Adieu, adieu, to {output} and {name_list[-1]}")
                break
         '''  
        try:
            name = input("Name: ").strip()
            if name:
                name_list.append(name)

        except EOFError:
            break

    if not name_list:
        return 
    if len(name_list) ==1:
        output = name_list[0]
    else:
        output = ", ".join(name_list[:-1]) + " and " +name_list[-1]

    print(f"\nAdieu, adieu, to {output}") 



if __name__ == "__main__":
    main()