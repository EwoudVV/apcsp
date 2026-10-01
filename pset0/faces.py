# convert ascii emojis into unicode ones

def convert():
    usrinput = input("put an ascii emoji here: ")

    if usrinput == ":)":
        print("🙂")
    elif usrinput == ":(":
        print("☹️")
    elif usrinput == ":D":
        print("😁")
    elif usrinput == ":3":
        print("🐱")
    elif usrinput == ":|":
        print("😐")
    elif usrinput == ":/":
        print("😕")

def main():
    convert()

if __name__ == "__main__":
	main()