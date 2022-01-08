class ATM_Card:
    def __init__(self, card_num, owned_by):
        self.__card_num = card_num
        self.__owned_by = owned_by

    def get_acct_types(self):
#   returns a list of the account types available for the customer.
        return self.__owned_by.get_acct_list

    def access(self, input_acct_type):
#   accepts an account type and returns the Account object of the customer
        return input_acct_type.get_type

    def __str__(self):
#   returns a string representation of the ATM card detailing the card's number and owner's name.
        return f"Card Number: {self.__card_num}, Owner: {self.__owned_by}"

    def get_card_num(self):
        return self.__card_num
    
    def owned_by(self):
        return self.__owned_by