#Function to take Product Name(s) as a list

#Function to take Product Price as a float (allow decimal NO INT)
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
#Function to take Product quantity as an INT

#Function to List Product Name with its appropriate price and quantity

#Make it look pretty (Optional bonus)


