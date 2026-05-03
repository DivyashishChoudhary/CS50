def main():
    total_inserted = 0
    print("Amount Due: 50")
    while True:
        coin_entry = int(input("Insert Coin: "))
        if coin_entry in {5,10,25}:
            total_inserted += coin_entry
            if total_inserted >= 50:
                print(f"Change Owed: {total_inserted - 50}")
                break
            else:
                print(f"Amount Due: {50 - total_inserted}")
        else:
            print(f"Amount Due: {50 - total_inserted}")


if __name__ == "__main__":
    main()