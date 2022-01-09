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
                    atm_menu_sys(atm_obj)
        elif option == "2":
            print("Goodbye")
            break

        def atm_menu_sys(atm_obj):
            print("""
            Available options
            1. Check balance
            2. Withdraw funds
            3. Transfer funds
            4. Return card""")
            #transact_option = input("Enter a transaction option: ")