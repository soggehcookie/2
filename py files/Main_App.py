def atm_app(atm_obj):
    while(True):
        print("Available options:\n1. Insert ATM card\n2.Quit simulation")
        option = input("Enter an option: ")
        if option == "1":
            card_num_in = input("Enter an ATM card number: ")
            if atm_obj.check_card(card_num_in) == False:
                print("Invalid card")   
            else:
                pin_num_in = input("Enter your pin number: ")
                if atm_obj.check_pin(pin_num_in) == False:
                    print("Invalid pin number")
                else:
                    return atm_menu_sys(atm_obj)
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
                else:
                    sys_menu_running = False 
            elif check_choice == "2":
                atm_obj.show_balance("Savings")
                print(atm_obj.show_balance("Savings"))
        #Withdraw funds
        elif transact_option == "2":
            print("Choose Account:\n1.Current Account\n2.Savings Account")
            withdraw_choice = input("Enter an account option: ")
            withdraw_amt = input("Enter amount to withdraw: ")
            withdraw_amt = float(withdraw_amt)
            if withdraw_choice == "1":
                atm_obj.transactions("withdraw", withdraw_amt, "Current")
                print(f"{atm_obj.show_balance('Current')}")
            elif withdraw_choice == "2":
                atm_obj.transactions("withdraw", withdraw_amt, "Savings")
                print(f"{atm_obj.show_balance('Savings')}")
        #Transfer funds
        elif transact_option == "3":
            print("Choose Account:\n1.Current Account\n2.Savings Account")
            xfer_choice = input("Enter an account option: ")
            xfer_acc = input("Enter the account number to transfer funds to: ")
            xfer_amt = input("Enter the amount to transfer: ")
            xfer_amt = float(xfer_amt)
            if xfer_choice == "1":
                current_count = 1
                while(current_count <= 3):
                    atm_obj.transactions("transfer", xfer_amt, "Current", xfer_acc)
                    if atm_obj.transactions("transfer", xfer_amt, "Current", xfer_acc) == True:
                        print(f"{atm_obj.show_balance('Current')}")
                        current_count += 3
                    else:
                        print(f"Kindly enter a valid transfer account.\nYou have {3 - current_count} tries left.")
                        current_count += 1
            elif xfer_choice == "2":
                savings_count = 1
                while(savings_count <= 3):
                    atm_obj.transactions("transfer", xfer_amt, "Savings", xfer_acc)
                    if atm_obj.transactions("transfer", xfer_amt, "Savings", xfer_acc) == True:
                        print(f"{atm_obj.show_balance('Savings')}")
                        savings_count += 3
                    else:
                        print(f"Kindly enter a valid transfer account.\nYou have {3 - savings_count} tries left.")
                        savings_count += 1
        elif transact_option == "4":
            break