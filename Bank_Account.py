class BankAccount:
    def __init__(self, int_rate = 0.01, acc_balance = 0):
        self.int_rate = int_rate
        self.balance = acc_balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - self.balance < 0:

            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

        self.balance -= amount

        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


matyas_account = BankAccount(0.01,100)
bryan_account = BankAccount(0.01, 50)

matyas_account.deposit(300).deposit(300).deposit(300).withdraw(200).yield_interest().display_account_info()
bryan_account.deposit(500).deposit(500).withdraw(340).withdraw(350).withdraw(50).withdraw(25).yield_interest().display_account_info()