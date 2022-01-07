import datetime
import Customer
import Account
from abc import ABC, abstractmethod

class ATM_Transaction(ABC):

    def __init__(self, transaction_type, date = datetime.datetime.now(), transaction_id = 0, amount = 0):
        self.transaction_id = transaction_id
        self.date = date
        self._transaction_type = transaction_type
        self._amount = amount

        transaction_id += 1

    @abstractmethod
    def update(self, account, amount, xfer_acct = None):
#   accepts the customer's Account object, amount (monetary value) and a transfer
#   account object (default value is None ) via input parameters. Implementation to be done by the child classes. 
#   (Hint: @abstractmethod)
        self.account = account
        self.amount = amount



class Withdrawl(ATM_Transaction):
    def __init__(self, amount, date, transaction_type = "withdrawl"):
        super().__init__(date, amount)

    def withdrawl(self, withdrawl_account):
#   accepts an Account object and calls the update() function with the appropriate parameters.
#   Returns the status of the update() function.
        self.update(withdrawl_account)
        if self.update(withdrawl_account) == True:
            return f"Update successful"
        

    def update(self, update_account):
#   function that updates the customer's Account object with the funds to be withdrawn.
#   Returns the status of the transaction.
        counter = 0
        if counter < 1:
            update_account.debit -= self._amount
            counter += 1
        if counter == 1:
            return f"Transaction successful"

class Transfer(ATM_Transaction):
    def __init__(self, amount, date = datetime.datetime.now(), transaction_type = "transfer"):
        super().__init__(date, amount)

    def update(self, xfer_account):
        count = 0
        if count < 1:
            xfer_account.credit += self._amount
            count += 1
        if count == 1:
            return f"Transfer successful"
