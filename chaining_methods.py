class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, amount, receiving_person):
        self.account_balance -= amount
        receiving_person.account_balance += amount
        return self


matyas = User('Matyas', 'matyas@asd.com')
hillary = User('Hillary', 'hills@asd.com')
bryan = User('Bryan', 'bryan@asd.com')


matyas.make_deposit(100).matyas.make_deposit(100).matyas.make_deposit(100)

matyas.make_withdrawal(200)

matyas.display_user_balance()

hillary.make_deposit(500).hillary.make_deposit(500)

hillary.make_withdrawal(200).hillary.make_withdrawal(200)

hillary.display_user_balance()

bryan.make_deposit(1000)

bryan.make_withdrawal(300).bryan.make_withdrawal(
    300).bryan.make_withdrawal(300)

bryan.display_user_balance()

hillary.transfer_money(100, bryan)

hillary.display_user_balance()
bryan.display_user_balance()
