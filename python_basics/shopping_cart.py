print("Shopping Cart")

list_name = []
list_price = []


def show_menu():
    print("\n1: Add item\n 2: View cart \n 3: Checkout \n 4: Exit")


while True:
    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many products do you want to add? "))

        for i in range(n):
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))

            list_name.append(name)
            list_price.append(price)

    elif choice == 2:
        print("\nShopping Cart :")

        if len(list_name) == 0:
            print("Your cart is empty")
        else:
            for i in range(len(list_name)):
                print(f"{i+1}. {list_name[i]} - ${list_price[i]:.2f}")

    elif choice == 3:
        print("\nReceipt : ")

        if len(list_name) == 0:
            print("Your cart is empty")
        else:
            total = 0

            for i in range(len(list_name)):
                print(f"{list_name[i]} - ${list_price[i]:.2f}")
                total += list_price[i]

            tax = total * 0.10
            final_total = total + tax

            print(f"\nSubtotal: ${total:.2f}")
            print(f"Tax (10%): ${tax:.2f}")
            print(f"Total: ${final_total:.2f}")

    elif choice == 4:
        print("Thank you for shopping with us!")
        break

    else:
        print("Please enter a number between 1 and 4")