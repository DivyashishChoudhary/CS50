def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print("\n")
            asc_item_list = sorted(grocery_list)
            
            for i in range(len(asc_item_list)):
                print(f"{grocery_list[asc_item_list[i]]} {asc_item_list[i].upper()}")
            
            break


main()