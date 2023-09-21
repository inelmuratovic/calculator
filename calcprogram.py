def get_price():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price;
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            return quantity
        except ValueError:
            print("Invalid decimal number. Please try again.")

def main():
    print("The Total Calculator Program\n")

    price = get_price()
    quantity = get_quantity()

    total = price * quantity

    print()
    print("PRICE:     ", price)
    print("QUANTITY:  ", quantity)
    print("TOTAL:     ", total)


if __name__ == "__main__":
    main()
