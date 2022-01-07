import Customer, Account

class ATM_Card:
    def __init__(self, card_num, card_owner):
        self.__card_num = card_num
        self.__card_owner = Account.get_owner()

    def get_acct_types(self):
        return Customer.get_acct_list

    def access(self, input_acct_type):
        self.input_acct_type = input_acct_type
        return Account.get_type(self.input_acct_type)

    def __str__(self):
        return f"Card Number: {self.__card_num}, Owner: {self.__card_owner}"

    def get_card_num(self):
        return self.__card_num
    
    def owned_by(self):
        return self.__card_owner