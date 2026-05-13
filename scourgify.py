import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Not the correct amount of inputs there")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit(".csv is expected in input and output files")
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
    except FileNotFoundError:
        sys.exit("File does not exist")
    with open(sys.argv[2],"w") as file:
        writer = csv.DictWriter(file,fieldnames =["first","last","house"])
        writer.writeheader()
        for row in rows:
            last, first = row["name"].split(", ", maxsplit=1)
            house = row["house"]
            writer.writerow({"first":first,"last":last,"house":house})

if __name__ == "__main__":
    main()