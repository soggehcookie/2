from Bank import Bank # from bank.py import Bank class
from ATM import ATM
from Account import Savings_Account, Current_Account
from ATM_Card import ATM_Card
from Customer import Customer
from Main_App import atm_app # from main_app.py import atm_app function
# set up the bank objects.
bank_01 = Bank("POSB01", "51 Sunset lane")
# set up atm object
atm_01 = ATM("tannery lane 78", bank_01)
# bank_01 has 1 atm
bank_01.maintains(atm_01)
# set up customer object.
# customer 1 has 1 savings acct with 8k and 1 current acct with 5k with bank_01
cust_01 = Customer('Tom', 'abc lane', '15-may-1987')
save_01 = Savings_Account("458-96252", cust_01)
curr_01 = Current_Account("124-87592", cust_01)
cust_01.owns(save_01)
cust_01.owns(curr_01)
# adding money to acct
save_01.credit(8000)
curr_01.credit(5000)
# ATM card
dc_01 = ATM_Card("589-5955-874-6941", cust_01)
bank_01.manages(dc_01)
bank_01.add_customer(cust_01, "1234")
# customer 2 has 1 savings acct with 6k with bank_01
cust_02 = Customer('Kim', 'blank lane', '05-dec-1999')
save_02 = Savings_Account("874-15268", cust_02)
cust_02.owns(save_02)
# adding money to acct
save_02.credit(6000)
# ATM card
dc_02 = ATM_Card("847-9521-248-8451", cust_02)
bank_01.manages(dc_02)
bank_01.add_customer(cust_02, "8745")
#print customer info
print(cust_01)
print(dc_01)
print(save_01.check_balance())
print(curr_01.check_balance())
print(cust_01.get_acct_list())
print()
print(cust_02)
print(dc_02)
print(save_02.check_balance())
print(cust_02.get_acct_list())
#start running the ATM using the atm_app function you created in main_app.py
atm_app(atm_01)

#Test Cases:
#1.Testing invalid pin number
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option: 1
# Enter an ATM card number: 589-5955-874-6941
# Enter your pin number: 545 
# Invalid pin number.

#2. Testing withdraw more funds than in account
# Enter a transaction option: 2
# Choose Account:
# 1.Current Account
# 2.Savings Account
# Enter an account option: 2
# Enter amount to withdraw: 10000
# Withdrawl not successful
# Invalid withdrawal amount. Kindly enter a valid withdrawal amount.
# You have 2 tries left

# Enter amount to withdraw: 10000
# Withdrawl not successful
# Invalid withdrawal amount. Kindly enter a valid withdrawal amount.
# You have 1 tries left

# Enter amount to withdraw: 10000
# Withdrawl not successful
# Invalid withdrawal amount. Kindly enter a valid withdrawal amount.
# You have 0 tries left

# No attempts left, returning to main menu.
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option:

#3.Testing transfer of funds to the same account
# Available options
# 1. Check balance
# 2. Withdraw funds
# 3. Transfer funds
# 4. Return card
# Enter a transaction option: 3
# Choose Account:
# 1.Current Account
# 2.Savings Account
# Enter an account option: 2
# Enter the account number to transfer funds to: 458-96252
# Enter the amount to transfer: 500
# Invalid account. Kindly enter a valid transfer account.
# You have 2 tries left.

# Enter the account number to transfer funds to: 458-96252
# Enter the amount to transfer: 500
# Invalid account. Kindly enter a valid transfer account.
# You have 1 tries left.

# Enter the account number to transfer funds to: 458-96252
# Enter the amount to transfer: 500
# Invalid account. Kindly enter a valid transfer account.
# You have 0 tries left.

# No attempts left, returning to main menu.
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option:

#4. Transferring amount that is more than balance in account
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option: 1
# Enter an ATM card number: 589-5955-874-6941
# Enter your pin number: 1234
# Available options
# 1. Check balance
# 2. Withdraw funds
# 3. Transfer funds
# 4. Return card
# Enter a transaction option: 3
# Choose Account:
# 1.Current Account
# 2.Savings Account
# Enter an account option: 1
# Enter the account number to transfer funds to: 874-15268
# Enter the amount to transfer: 10000
# Insufficient funds. Returning to main menu.
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option:

# #5. Transferring to non-existent account
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option: 1
# Enter an ATM card number: 589-5955-874-6941
# Enter your pin number: 1234
# Available options
# 1. Check balance
# 2. Withdraw funds
# 3. Transfer funds
# 4. Return card
# Enter a transaction option: 3
# Choose Account:
# 1.Current Account
# 2.Savings Account
# Enter an account option: 2
# Enter the account number to transfer funds to: 12345
# Enter the amount to transfer: 500
# Account not found. Kindly enter a valid transfer account.
# You have 2 tries left.
# Enter the account number to transfer funds to: 12345
# Enter the amount to transfer: 500
# Account not found. Kindly enter a valid transfer account.
# You have 1 tries left.
# Enter the account number to transfer funds to: 12345
# Enter the amount to transfer: 500
# Account not found. Kindly enter a valid transfer account.
# You have 0 tries left.
# No attempts left, returning to main menu.
# Available options:
# 1. Insert ATM card
# 2.Quit simulation
# Enter an option: