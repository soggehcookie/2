class Customer:
    def __init__(self, name, address, dob, acct_list = []):
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__acct_list = acct_list
        

    def owns(self, account):
        if account not in self.__acct_list:
            self.__acct_list.append(account)

    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}, Date of birth: {self.__dob}"

    def get_name(self):
        return self.__name

    def get_acct_list(self):
        return self.__acct_list
