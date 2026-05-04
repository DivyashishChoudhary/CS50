price_list = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
def main():
    total_cost = 0
    while True:
        try:
            dish = input("Item: ").strip().title()
            total_cost += price_list[dish]
            print(f"Total: ${total_cost:.2f}")

        except EOFError:
            print(f"\nTotal: ${total_cost:.2f}")
            break
        except KeyError:
            continue

main()
