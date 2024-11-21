import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    inp_url = re.match(r"^.*src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\".*$", s)
    return f"https://youtu.be/{inp_url.group(1)}" if inp_url else None

if __name__ == "__main__":
    main()
