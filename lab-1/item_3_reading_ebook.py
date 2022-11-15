def main():
    print("*** Reading E-Book ***")
    print("Text , Highlight : ", end="")

    txt, hl = input().split(",")
    txt = txt.replace(hl, "["+hl+"]")
    print(txt)

if __name__ == "__main__":
    main()
