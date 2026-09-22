import re
import sys

def main():

    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search( r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$", ip):
        if  (0 <= int(matches.group(1)) <= 255) and (0 <= int(matches.group(2)) <= 255) and (0 <= int(matches.group(3)) <= 255) and (0 <= int(matches.group(4)) <= 255):
            return True
    return False


if __name__ == "__main__":
    main()
