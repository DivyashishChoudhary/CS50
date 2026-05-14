import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        ip1, ip2, ip3, ip4 = matches.groups()
        ip1, ip2, ip3, ip4 = int(ip1),int(ip2),int(ip3),int(ip4)

        if ip1 not in range(256) or ip2 not in range(256) or ip3 not in range(256) or ip4 not in range(256):
            return False
        else:
            return True
    else:
        return False
    

    


if __name__ == "__main__":
    main()