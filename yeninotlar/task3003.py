class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance

account1 = BankAccount("AZ123456789", 1000, "2022-01-01", "John")
account2 = BankAccount("AZ987654321", 2000, "2022-02-01", "Jane")
account3 = BankAccount("AZ567890123", 3000, "2022-03-01", "Mike")
account4 = BankAccount("AZ432109876", 4000, "2022-04-01", "Emily")

print(account1.deposit(500))
print(account2.withdraw(1500))
print(account3.check_balance())
print(account4.check_balance())