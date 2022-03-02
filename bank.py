import random
class BankAccount:
    def __init__(self, number, name, acc_type, balance):
        self.number = number
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
       
    def withdraw(self, amount):
        if(amount>self.balance):
            return False
        self.balance-=amount
        return True
           
    def deposit(self, amount):
        self.balance+=amount
        return True
   
    def account_details(self):
        print(f"Number: \t{self.number}\nName: \t{self.name}\nType: \t{self.acc_type}\nBalance: \t{self.balance}")
   
usr_name = input("Enter your name: ")
account_type = int(input("Enter the type of the account\n 1. savings \t 2. credit: "))
balance = int(input("Enter the amount to be initially deposited: "))

account = BankAccount(random.randint(0, 10), usr_name, account_type==1 and "savings" or "credit", balance)
choice = 0
while(choice!=4):
    choice = int(input("Enter your choice \n 1. deposit \t 2. withdraw \t 3.details \t 4.exit: "))
    if(choice == 1):
        if account.deposit(int(input("Enter the amount to deposit: "))):
            print(f"Amount deposited\n Current balance: {account.balance}")
    elif(choice == 2):
        if not account.withdraw(int(input("Enter the amount to withdraw: "))):
            print(f"Not enough balance\n Current balance:  {account.balance}")
            continue
        print(f"Amount withdrawn\n Current balance: {account.balance}")
    elif(choice == 3):
        account.account_details()
