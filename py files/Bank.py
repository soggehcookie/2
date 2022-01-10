import random
from Additional_Exceptions import InvalidPinNumber, AccountNotFound

class Bank:
    def __init__(self, code, address, atm_list = [], customer_list = [], card_list = []):
#   code - private variable, a bank code
#   address - private variable, bank's address
#   list of ATM - a list of ATM objects
#   list of customers - a list of Customer records
#   list of atm cards - a list of ATM_card objects
        self.__code = code
        self.__address = address
        self.atm_list = atm_list
        self.customer_list = customer_list
        self.card_list = card_list

    def add_customer(self, customer, cust_pin):
        self.customer = customer
        cust_id = self.customer.get_name() + str(random.randint(0000, 9999))
        cust_obj = self.customer
        keyname_id = self.customer.get_name() + "_id"
        keyname_obj = self.customer.get_name() + "_obj"
        keyname_pin = self.customer.get_name() + "_pin"
        person_key = [keyname_id, keyname_obj, keyname_pin]
        person_value = [cust_id, cust_obj, cust_pin]
        person_dict = dict(zip(person_key, person_value))
        self.customer_list.append(person_dict)

    def manages(self, atm_card):
    #accepts an atm_card object and stores it in the list of atm cards.
        self.card_list.append(atm_card)

    def maintains(self, atm):
    #accepts an ATM object and stores it in the list of ATMs.
        self.atm_list.append(atm)

    def authorize_pin(self, customer, input_pin):
    #accepts a customer's object and pin number as input parameters,
    #checks that the customer's pin number is valid. Returns a True if the pin number is valid
    #otherwise raises a InvalidPinNumber exception (Enter a pin from main.py)
        for dicts in self.customer_list:
            if customer in dicts.values():
                if input_pin in dicts.values():
                    return True
                else:
                    raise InvalidPinNumber()

    def get_acct(self, input_acct_num):
    #accepts an account number as input parameter and check if the account number is valid
    #Returns an Account object if the account number is valid otherwise raises a AccountNotFound exception.
        for cust_obj in self.card_list:
            for acc_obj in cust_obj.owned_by().get_acct_list():
                if input_acct_num in acc_obj:
                    return acc_obj
                else:
                    raise AccountNotFound()

    def get_card_list(self):
        return self.card_list