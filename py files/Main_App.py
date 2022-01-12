from Additional_Exceptions import InsufficientFunds, InvalidAccount, InvalidPinNumber, InvalidATMCard, AccountNotFound
def atm_app(atm_obj):
    while(True):
        print("Available options:\n1. Insert ATM card\n2.Quit simulation")
        option = input("Enter an option: ")
        if option == "1":
            card_num_in = input("Enter an ATM card number: ")
            try:
                if atm_obj.check_card(card_num_in) == True:
                    pin_num_in = input("Enter your pin number: ")
                    try:
                        if atm_obj.check_pin(pin_num_in) == True:
                            atm_menu_sys(atm_obj)
                    except InvalidPinNumber:
                        print("Invalid pin number.\n")
                        break
            except InvalidATMCard:
                print("Invalid ATM Card number. Kindly take your card.\n")
                break
                    
        elif option == "2":
            print("Goodbye")
            break
    
def atm_menu_sys(atm_obj):
    sys_menu_running = True
    while(sys_menu_running):
        print("Available options\n1. Check balance\n2. Withdraw funds\n3. Transfer funds\n4. Return card")     
        transact_option = input("Enter a transaction option: ")

        #Checking balance
        if transact_option == "1":
            print("Choose Account:\n1.Current Account\n2.Savings Account")
            check_choice = input("Enter an account option: ")
            if check_choice == "1":
                if atm_obj.check_accts() == True:
                    atm_obj.show_balance("Current")
                    print(atm_obj.show_balance("Current"))
                    print()
                else:
                    print("You do not have a Current account.\n")
                    sys_menu_running = False
                    atm_app(atm_obj) 
            elif check_choice == "2":                 #default all accounts have savings so no need to check_accts
                atm_obj.show_balance("Savings")
                print(atm_obj.show_balance("Savings"))
                print()

        #Withdraw funds
        elif transact_option == "2":
            print("Choose Account:\n1.Current Account\n2.Savings Account")
            withdraw_choice = input("Enter an account option: ")            
            if withdraw_choice == "1":
                withdraw_curr_count = 0
                while(withdraw_curr_count < 4):
                    withdraw_curr_amt = input("Enter amount to withdraw: ")
                    withdraw_curr_amt = float(withdraw_curr_amt)
                    if atm_obj.transactions("withdraw", withdraw_curr_amt, "Current") == True:
                        print(f"{atm_obj.show_balance('Current')}\n")
                        withdraw_curr_count += 4
                    else:
                        print(f"Invalid withdrawal amount. Kindly enter a valid withdrawal amount.\nYou have {2 - withdraw_curr_count} tries left\n")
                        withdraw_curr_count += 1
                        if withdraw_curr_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)
            elif withdraw_choice == "2":
                withdraw_sav_count = 0
                while(withdraw_sav_count < 4):
                    withdraw_sav_amt = input("Enter amount to withdraw: ")
                    withdraw_sav_amt = float(withdraw_sav_amt)
                    if atm_obj.transactions("withdraw", withdraw_sav_amt, "Savings") == True:
                        print(f"{atm_obj.show_balance('Savings')}\n")
                        withdraw_sav_count += 4
                    else:
                        print(f"Invalid withdrawal amount. Kindly enter a valid withdrawal amount.\nYou have {2 - withdraw_sav_count} tries left\n")
                        withdraw_sav_count += 1
                        if withdraw_sav_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)

        #Transfer funds
        elif transact_option == "3":
            print("Choose Account:\n1.Current Account\n2.Savings Account")
            xfer_choice = input("Enter an account option: ")
            if xfer_choice == "1":
                current_count = 0
                while(current_count < 4):
                    xfer_acc_curr = input("Enter the account number to transfer funds to: ")
                    xfer_amt_curr = input("Enter the amount to transfer: ")
                    xfer_amt_curr = float(xfer_amt_curr)
                    try:
                        if atm_obj.transactions("transfer", xfer_amt_curr, "Current", xfer_acc_curr) == True:
                            print(f"{atm_obj.show_balance('Current')}")
                            current_count += 4
                    except InsufficientFunds:
                        print(f"Insufficient funds. Returning to main menu.")
                        current_count += 4
                        atm_app(atm_obj)
                    except InvalidAccount:
                        print(f"Invalid account. Kindly enter a valid transfer account.\nYou have {2 - current_count} tries left.")
                        current_count += 1
                        if current_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)
                    except AccountNotFound:
                        print(f"Account not found. Kindly enter a valid transfer account.\nYou have {2 - current_count} tries left.")
                        current_count += 1
                        if current_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)
            elif xfer_choice == "2":
                savings_count = 0
                while(savings_count < 4):
                    xfer_acc_sav = input("Enter the account number to transfer funds to: ")
                    xfer_amt_sav = input("Enter the amount to transfer: ")
                    xfer_amt_sav = float(xfer_amt_sav)
                    try:
                        if atm_obj.transactions("transfer", xfer_amt_sav, "Savings", xfer_acc_sav) == True:
                            print(f"{atm_obj.show_balance('Savings')}\n")
                            savings_count += 4
                    except InsufficientFunds:
                        print(f"Insufficient funds. Returning to main menu.")
                        savings_count += 4
                        atm_app(atm_obj)
                    except InvalidAccount:
                        print(f"Invalid account. Kindly enter a valid transfer account.\nYou have {2 - savings_count} tries left.")
                        savings_count += 1
                        if savings_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)
                    except AccountNotFound:
                        print(f"Account not found. Kindly enter a valid transfer account.\nYou have {2 - savings_count} tries left.")
                        savings_count += 1
                        if savings_count == 3:
                            print("No attempts left, returning to main menu.")
                            atm_app(atm_obj)
        elif transact_option == "4":
            atm_app(atm_obj)