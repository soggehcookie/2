from ATM_Transaction import Withdrawl, Transfer
from Additional_Exceptions import InvalidAccount, InvalidATMCard, InvalidPinNumber

class ATM:
    def __init__(self, atm_location, managed_by, current_card = None):
#   constructor that initializes the ATM's location and managed by attributes via input parameters.
#   current card - private variable, the current ATM card that is "inserted" by the user of the ATM.
#   The attribute current card is set to None .

        self.atm_location = atm_location
        self.managed_by = managed_by
        self.__current_card = current_card

    def get_current_card(self):
        return self.__current_card

    def transactions(self, transaction_type, amount, acct_type, xfer_acct_num = None):
#   accepts transaction type, amount, account type and transfer account number 
#   which has a default value of None via input parameters. Process the requested
#   transaction according to the transaction type. Returns the status of the respective
#   transactions or raises an exception indicating whether or not the transactions were successful.
        #if acct_type in self.__current_card.get_acct_types:
        self.user_obj = self.__current_card.access(acct_type)
        if transaction_type == "withdraw":
            try:
                withdraw_obj = Withdrawl(amount)
                return withdraw_obj.withdrawl(self.user_obj)
            except:
                print(f"Withdrawl not successful")

        elif transaction_type == "transfer":
            xfer_acct_obj = self.managed_by.get_acct(xfer_acct_num)
            if self.user_obj == xfer_acct_obj:
                raise InvalidAccount()

            else:
                xfer_obj = Transfer(amount)
                xfer_obj.update(self.user_obj, xfer_acct_obj)
                return True
            

    def check_accts(self):
#   checks if the user has 1 or 2 accounts. Returns True if there is 2 otherwise returns False.
        # for i in (self.__current_card.get_acct_types()):
        if len(self.__current_card.get_acct_types()) == 2:
            return True
        else:
            return False 

    def check_pin(self, input_pin_num):
#   accepts a user's pin number and checks with the bank if it is valid. 
#   Returns the status of the check from the bank.
        self.managed_by.authorize_pin(self.__current_card.owned_by(), input_pin_num)
        return True

    def check_card(self, input_card_num):
#   accepts a ATM card number and checks with the bank if the card is a valid card.
#   If it is valid, the current card attribute is set to this ATM card object and returns True
#   but if the card is invalid, raise an InvalidATMCard exception.
        check_var = 0
        for l in self.managed_by.get_card_list():
            if input_card_num == l.get_card_num():
                check_var = 1
                self.__current_card = l
                return True
        if check_var == 0:
            raise InvalidATMCard()

    def show_balance(self, acct_type):
#   accepts an Account type and 
#   returns a string message detailing the current balance of the requested account of that customer
        if acct_type == "Savings":
            acc = self.__current_card.access("Savings")
        elif acct_type == "Current":
            acc = self.__current_card.access("Current")
        return f"Your {acct_type} account has a balance of ${acc.check_balance()}"