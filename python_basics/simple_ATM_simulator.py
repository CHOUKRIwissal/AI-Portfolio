print("ATM SIMULATOR \n")
current_balance = 1000.0  # Initial balance
history = []
# Display the ATM menu
def show_menu():
    print("\n Please select an option: \n  1. Check Balance \n 2. Deposit Money \n 3. Withdraw Money \n 4. Transaction History \n 5. Exit")
# Main program loop
while True:
    show_menu()
    choice=int(input("\n Enter your choice: "))
    if choice==1: 
        print(f"Current Balance: ${current_balance:.2f}")
    elif choice==2: 
        deposit=float(input(f"Enter deposit amount:"))
        if deposit <= 0: 
            print("Invalid amount")
        elif deposit> 1000: 
            print("Cannot deposit more than $1000")
        else: 
            print(f"{deposit} deposited successfully!")
            current_balance += deposit
            history.append(f"Deposited ${deposit:.2f}")
            print(f"New Balance: {current_balance:.2f}")
    elif choice==3:
        withdraw=float(input(f"Enter withdraw amount:"))
        
        if withdraw <= 0:
            print("Invalid amount.")                    
        elif withdraw> current_balance:
            print("Cannot withdraw more than balance")
        elif withdraw> 500:
            print("Cannot withdraw more than $500 per transaction")
        elif withdraw<10:
            print("Minimum withdrawal: $10")
        else:
            print(f"{withdraw} withdrawed successfully!")
            current_balance -= withdraw
            history.append(f"Withdrew ${withdraw:.2f}")
            print(f"New Balance: {current_balance:.2f}")
    elif choice == 4:

        print("\nTransaction History")
        if len(history) == 0:
            print("No transactions.")
        else:
            for transaction in history:
                print(transaction)
    elif choice == 5:
        print("\nThank you for using our ATM.")
        break
    else:
        print("Invalid menu choice.")
    
    input("\nPress Enter to continue...")