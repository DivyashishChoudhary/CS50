import sys
import csv
import tabulate

def main():
    if len(sys.argv) !=2:
        sys.exit("Need exactly one input which is file name")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        table = tabulate.tabulate(rows,headers="keys", tablefmt="grid")
        print(table)
        










if __name__ == "__main__":
    main()