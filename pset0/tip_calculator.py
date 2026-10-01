def main():
    dollars = input("how much was the meal? ")
    percent = input("what percentage do you want to tip? ")

    dollars = dollars_to_float(dollars)
    percent = percent_to_float(percent)

    tip = dollars * percent
    total = dollars + tip

    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")


def dollars_to_float(str_dollar):
    str_dollar = str_dollar.replace("$", "")
    return float(str_dollar)


def percent_to_float(str_percent):
    str_percent = str_percent.replace("%", "")
    return float(str_percent) / 100


if __name__ == "__main__":
    main()