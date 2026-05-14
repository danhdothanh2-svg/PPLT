class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount} successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount} successfully.")
        else:
            print("Withdrawal failed. Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


# Create a BankAccount object
# Account number 1
account1 = BankAccount("Do Thanh Danh")

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(400)  

print("Current Balance:", account1.get_balance())

# Account number 2
account2 = BankAccount("Do Thanh Duy")

account2.deposit(1000)
account2.withdraw(500) 
account2.withdraw(400)
account2.withdraw(300)

print("Current Balance:", account2.get_balance())