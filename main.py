def displayMenu():
    print("Welcome to Taco Palace! please view the menu below and enter the number that represents your selection")
    print()
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos ")
    print("4. Soft Drink")
    print("5. Quit")
    print()

def getPrice(itemNumber):
    if itemNumber == 1:
        return 2.55
    elif itemNumber == 2:
        return 3.99
    elif itemNumber == 3:
        return 2.99
    elif itemNumber == 4:
        return 1.95
    else:
        return 0.00

selectedItems = []
totalPrice = 0.00

displayMenu()

while True:
    try:
        userInput = int(input("User entered: "))
        if userInput == 5:
            break
        if userInput in[1, 2, 3, 4]:
            itemPrice = getPrice(userInput)

            if userInput == 1:
                selectedItems.append("Taco")
            elif userInput == 2:
                selectedItems.append("Burrito")
            elif userInput == 3:
                selectedItems.append("Nachos")
            elif userInput == 4:
                selectedItems.append("Soft Drink")

            totalPrice += itemPrice

            print(f"You selected a {selectedItems[-1]}.\n")
        else:
            print("Invalid selection. Please enter a number between 1 and 5.\n")

        displayMenu()

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

if selectedItems:
    print(f"You ordered a {', '.join(selectedItems)}. Your total is ${totalPrice: }\n")
else:
    print("No items were ordered. Thank you for visiting Taco Palace!\n")