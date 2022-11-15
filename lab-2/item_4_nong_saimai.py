def main():
    year = int(input("Enter year : "))
    print(hbd(year))

def hbd(year):
    base = year // 2
    age = 20 + (year % 2)
    return "saimai is just %d, in base %d!" % (age, base)

if __name__ == "__main__":
    main()
