def atm_app(atm_obj):
    while(True):
        print("""
        Available options: 
        1. Insert ATM card
        2.Quit simulation""")
        option = input("Enter an option")

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
        print("""
        Available options
        1. Check balance
        2. Withdraw funds
        3. Transfer funds
        4. Return card""")
        transact_option = input("Enter a transaction option: ")
        if transact_option == "1":
            print("""
            Choose Account:
            1.Current Account
            2.Savings Account""")
            check_choice = input("Enter an account option: ")
            if check_choice == "1":
                if atm_obj.check_accts == True:
                    atm_obj.show_balance("Current")
                else:
                    sys_menu_running = False 
            elif check_choice == "2":
                atm_obj.show_balance("Savings")
        elif transact_option == "2":
            print("""
            Choose Account:
            1.Current Account
            2.Savings Account""")
            withdraw_choice = input("Enter an account option: ")
            if withdraw_choice == "1":
                withdraw_current = input("Enter amount to withdraw: ")
                atm_obj.transactions("withdraw", withdraw_current, "Current")
                atm_obj.show_balance("Current")
            elif withdraw_choice == "2":
                withdraw_savings = input("Enter amount to withdraw: ")
                atm_obj.transactions("withdraw", withdraw_savings, "Current")
                atm_obj.show_balance("Savings")