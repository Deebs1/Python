class Bank:
    def __init__(self):
        self.customers = {}
    def create_account(self, account_number, initial_balance = 0):
        if account_number in self.customers:
            print("Account number already exits")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully")

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("deposit successful")
        else:
            print("account number does not exist")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number]-=amount
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        else:
            print("account number doesnot exist")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("account doesnot exist")

bank = Bank()
acno = "SB-123"
amt = 1000
bank.create_account(acno, amt)
damt = 600
bank.make_deposit(acno, damt)
wamt = 500
bank.make_withdrawal(acno, wamt)
bank.check_balance(acno)

