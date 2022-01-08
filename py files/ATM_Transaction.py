import datetime
import Customer
import Account
from abc import ABC, abstractmethod

class ATM_Transaction(ABC):

    def __init__(self, transaction_type, date = datetime.datetime.now(), transaction_id = 0, amount = 0):
        self._transaction_type = transaction_type
        self.transaction_id = transaction_id
        self.date = date
        self._amount = amount

        transaction_id += 1

    @abstractmethod
    def update(self, account, amount, xfer_acct = None):
#   accepts the customer's Account object, amount (monetary value) and a transfer
#   account object (default value is None ) via input parameters. Implementation to be done by the child classes. 
#   (Hint: @abstractmethod)
        self.account = account
        self.amount = amount
        self.xfer_acct = xfer_acct

class Withdrawl(ATM_Transaction):
    def __init__(self, amount, date, transaction_type = "withdrawl"):
        super().__init__(amount, date)
        self.transaction_type = transaction_type

    def withdrawl(self, withdrawl_account):
#   accepts an Account object and calls the update() function with the appropriate parameters.
#   Returns the status of the update() function.
        if withdrawl_account in Customer.get_acct_list:
            self.update(withdrawl_account)
        if self.update() == True:
            return f"Update successful"
        
    def update(self):
#   function that updates the customer's Account object with the funds to be withdrawn.
#   Returns the status of the transaction.
        super.update()
        counter = 0
        if counter < 1:
            self.account.debit = self._amount
            counter += 1
        if counter == 1:
            return f"Transaction successful"

class Transfer(ATM_Transaction):
    def __init__(self, amount, date, transaction_type = "transfer"):
#   constructor that initializes the transaction's date & time (timestamp) by using
#   one of the datatime functions and transaction type set to 'transfer' . The attribute
#   amount via input parameters
        super().__init__(amount, date)
        self.transaction_type = transaction_type

    def update(self):
#   function that updates the customer's Account object with funds for the transfer process.
#   Returns True if successful.
        super().update()
        count = 0
        if self.xfer_acct in Customer.get_acct_list:
            if count < 1:
                self.xfer_acct.credit = self._amount
                count += 1
        if count == 1:
            return f"Transfer successful"
