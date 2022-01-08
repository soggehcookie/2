import ATM_Card
from ATM_Transaction import Withdrawl, Transfer
from Additional_Exceptions import InvalidAccount

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
        if acct_type in ATM_Card.get_acct_types:
            if transaction_type == "withdrawl":
                Withdrawl.withdrawl(amount)
                return Withdrawl.update(amount)
            elif transaction_type == "transfer":
                for accts in self.__current_card.get_acct_list:
                    if  xfer_acct_num is not accts:
                        Transfer.update(amount)
                        return Transfer.update(amount)
                    else:
                        raise InvalidAccount()

    def check_accts(self):
#   checks if the user has 1 or 2 accounts. Returns True if there is 2 otherwise returns False.
