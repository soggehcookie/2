# This script will house all the special exceptions that is created for this simulation. This script will have 5 classes:
# InvalidAccount , AccountNotFound , InsufficientFunds , InvalidATMCard and InvalidPinNumber.
# All are children of the Exception class.


# class MonthlySalaryNotInRange(Exception):
#     pass

# def check_salary(salary):
#     if salary > 6000:
#         raise MonthlySalaryNotInRange()
		

# salary = int(input("Enter salary amount for the month: "))

# try:
#     check_salary(salary)
# except MonthlySalaryNotInRange:
#     print("Invaid salary value")


class InsufficientFunds(Exception):
    #  print("You have insufficient funds in your account.")
    def __init__(self, msg = "You have insufficient funds in your account."):
        self.msg = msg

    def __str__(self):
        return f"{self.msg}"
    # pass

class InvalidATMCard(Exception):
    pass

class InvalidPinNumber(Exception):
    pass

class AccountNotFound(Exception):
    pass

class InvalidAccount(Exception):
    pass