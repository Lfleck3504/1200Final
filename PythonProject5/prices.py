def prices():
    price = []
    print('Type the word "quit" when you are done')
    while True:
        userinput = input("Enter price: ")
        if userinput.lower() == "quit":
            break

        price.append(float(userinput))
    print("price listed:")
    for p in price:
        print(p)

prices()