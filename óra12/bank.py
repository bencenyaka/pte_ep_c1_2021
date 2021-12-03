class BankAccount:
    def __init__(self, name: str, account_number: str, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyenleg(self):
        print(self.balance)

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawal(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print("Sikeres pénzfelvétel.")
        else:
            print("Nincs elegendő összeg.")

x=BankAccount("Géza","111",10000)
x2=BankAccount("Jani","000",2000)
x.egyenleg()
x2.egyenleg()
x.withdrawal(5000)
x2.withdrawal(5000)
x.egyenleg()
x2.egyenleg()
x.deposit(5000)
x2.deposit(5000)
x.egyenleg()
x2.egyenleg()