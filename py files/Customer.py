class Customer:
    def __init__(self, name, address, dob):
#   name - customer's name
#   address - customer's address
#   date of birth - customer's date of birth in datetime format (DD-MMM-YYYY)
#   list of accounts - a list of accounts a customer can have, maximum is 2. Savings and/or Current account/s
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.acct_list = []
        

    def owns(self, account):
#   owns() - accepts an Account object and adds it to the list. Max 2 accounts either savings and/or current
        if len(self.acct_list) < 2:
            self.acct_list.append(account)

    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}, Date of birth: {self.__dob}"

    def get_name(self):
        return self.__name

    def get_acct_list(self):
        return self.acct_list
