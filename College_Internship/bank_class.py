class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print("-----------------------------------")
        print("Bank Account Details:")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("----------------------------------")

#take user input for account number and balance
account_number = input("Enter the account number: ")    
balance = float(input("Enter the initial balance: "))

#create an instance of BankAccount
account = BankAccount(account_number, balance)

#take user input for deposit amount
deposit_amount = float(input("Enter the deposit amount: "))

#perform deposit
account.deposit(deposit_amount)

#display update balance
account.display_balance()