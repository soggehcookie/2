import datetime
from abc import ABC, abstractmethod

class ATM_Transaction(ABC):

    def __init__(self, transaction_type, amount = 0):
        self._transaction_type = transaction_type
        self.transaction_id = 0
        self.date = datetime.datetime.now()
        self._amount = amount

        self.transaction_id += 1

    @abstractmethod
    def update(self, account, amount, xfer_acct = None):
#   accepts the customer's Account object, amount (monetary value) and a transfer
#   account object (default value is None ) via input parameters. Implementation to be done by the child classes. 
#   (Hint: @abstractmethod)
        self.account = account
        self.amount = amount
        self.xfer_acct = xfer_acct

class Withdrawl(ATM_Transaction):
    def __init__(self, amount, transaction_type = "withdrawl"):
        super().__init__(amount)
        self.transaction_type = transaction_type

    def withdrawl(self, withdrawl_account):
#   accepts an Account object and calls the update() function with the appropriate parameters.
#   Returns the status of the update() function.
        if withdrawl_account in withdrawl_account.get_owner().get_acct_list():
            return self.update()

        
    def update(self):
#   function that updates the customer's Account object with the funds to be withdrawn.
#   Returns the status of the transaction.
        return self.account.debit(self._amount)

class Transfer(ATM_Transaction):
    def __init__(self, amount, transaction_type = "transfer"):
#   constructor that initializes the transaction's date & time (timestamp) by using
#   one of the datatime functions and transaction type set to 'transfer' . The attribute
#   amount via input parameters
        super().__init__(amount)
        self.transaction_type = transaction_type

    def update(self):
#   function that updates the customer's Account object with funds for the transfer process.
#   Returns True if successful.
        if self.xfer_acct in self.xfer_acct.get_owner.get_acct_list:
            if self.account.get_acct_num is not self.xfer_acct.get_acct_num:
                self.account.debit(self._amount)
                self.xfer_acct.credit(self._amount)
                return True
            # if cust_acct.debit(amount):
            #     transfer_acct.credit(amount)

