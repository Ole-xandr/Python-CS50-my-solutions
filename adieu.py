import inflect
p = inflect.engine()

# Input names, make an Oxford Commas list of them and print it:
def main():
    name_list = name_input()
    adieu_list = oxford_comma(name_list)
    print("Adieu, adieu, to", adieu_list)

# Input names and make a list of them:
def name_input():
    names = []
    while True:
        try:
            name = str(input()).strip()
            names.append(name)
        except(EOFError):
            break
    return names

# Make an Oxford Commas list of the names list:
def oxford_comma(l):
    mylist = p.join((l))
    return mylist

if __name__ == "__main__":
    main()
