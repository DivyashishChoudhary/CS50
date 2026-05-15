import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(emb):
    if matches := re.search(r"^https?://(www\.)?youtube\.com/embed/(\w+)$",emb,re.IGNORECASE):
        return ("https://youtu.be/"+matches.group(2))
    else:
        return None


if __name__ == "__main__":
    main()