import Customer
import random
import ATM_Card
from Additional_Exceptions import InvalidPinNumber, AccountNotFound

class Bank:
    def __init__(self, code, address, atm_list = [], customer_list = [], card_list = []):
        self.__code = code
        self.__address = address
        self.atm_list = atm_list
        self.customer_list = customer_list
        self.card_list = card_list

    def add_customer(self, customer, cust_pin):
        cust_id = customer.get_name() + str(random.randint(0000, 9999))
        cust_obj = customer
        keyname_id = customer.get_name() + "_id"
        keyname_obj = customer.get_name() + "_obj"
        keyname_pin = customer.get_name() + "_pin"
        person_key = [keyname_id, keyname_obj, keyname_pin]
        person_value = [cust_id, cust_obj, cust_pin]
        person_dict = dict(zip(person_key, person_value))
        self.customer_list.append(person_dict)

    def manages(self, atm_card):
    #accepts an atm_card object and stores it in the list of atm cards.
        self.card_list.append(atm_card)

    #def maintains(self):
    #accepts an ATM object and stores it in the list of ATMs.

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
        for info in Customer.get_acct_list:
            if input_acct_num in info:
                return info
            else:
                raise AccountNotFound()
