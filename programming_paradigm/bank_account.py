class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

        def deposit(self, amount):
            if amount > 0:
                self.account_balance += amount
                return f"Deposited: ${amount:.2f}. New balance: ${self.account_balance:.2f}"
            else:
                return "Deposit amount must be positive."

        def withdraw(self, amount):
            if 0 < amount <= self.account_balance:
                self.account_balance -= amount
                return true 
            else:
                return False

        def get_balance(self):
            return f"Current balance: ${self.account_balance:.2f}"