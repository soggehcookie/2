class ATM_Card:
    def __init__(self, card_num, owned_by):
#   card number - private variable, the ATM card's number
#   owned by - private variable, a Customer object
        self.__card_num = card_num
        self.__owned_by = owned_by

    def get_acct_types(self):
#   returns a list of the account types available for the customer.
        type_list = []
        if len(self.__owned_by.get_acct_list()) == 1:
            type_list = ["Savings"]
            return type_list
        elif len(self.__owned_by.get_acct_list()) == 2:
            type_list = ["Savings", "Current"]
            return type_list

    def access(self, input_acct_type):
#   accepts an account type and returns the Account object of the customer
        for i in self.__owned_by.get_acct_list():
            if input_acct_type == i.get_type():
                return i 

    def __str__(self):
#   returns a string representation of the ATM card detailing the card's number and owner's name.
        return f"Card Number: {self.__card_num}, Owner: {self.__owned_by}"

    def get_card_num(self):
        return self.__card_num
    
    def owned_by(self):
        return self.__owned_by