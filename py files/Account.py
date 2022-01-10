from Additional_Exceptions import InsufficientFunds

class Account:
    def __init__(self, acct_type, owner):
#   account type - protected variable. Values are either 'savings' or 'current'
#   owner - private variable. A Customer object
#   balance - private variable. Account balance
        self._acct_type = acct_type
        self.__owner = owner
        self.__balance = 0

    def check_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def get_type(self):
        return self._acct_type

    def debit(self, debit_amt):
#   accepts an amount, checks it then subtracts it from the balance. 
#   Returns True if there is enough funds for the debit otherwise, raise an exception
        if self.__validate_amount(debit_amt) == True:
            if self.__balance - debit_amt >= 0:
                self.__balance = self.__balance - debit_amt
                return True
            else:
                raise InsufficientFunds()


    def credit(self, credit_amt):
#   accepts an amount, checks it then adds it to the balance.
        if self.__validate_amount(credit_amt) == True:
            self.__balance = self.__balance + credit_amt
            return self.__balance

    def __validate_amount(self, input_amt):
#   accepts a monetary amount (be it of type integer or
#   float or string ), converts it to type float . Raise a ValueError if the monetary amount
#   is <= 0 or the amount has more than 2 decimal places. Return True otherwise
            self.input_amt = float(input_amt)
            if self.input_amt <= 0 or str(self.input_amt)[::-1].find(".") > 2:
                raise ValueError("Please enter a valid amount.")
            else:
                return True


class Savings_Account(Account):
    def __init__(self, acc_num, owner, acct_type = "Savings"):
#   account number - private variable. The account number of the respective account
#   owner - a Customer object
        super().__init__(acct_type, owner)
        self.__acc_num = acc_num

    def get_acc_num(self):
        return self.__acc_num

class Current_Account(Account):
    def __init__(self, acc_num, owner, acct_type = "Current"):
        super().__init__(acct_type, owner)
        self.__acc_num = acc_num
        
    def get_acc_num(self):
        return self.__acc_num   
