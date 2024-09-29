# banking app 
#claass based
#withdrawl and deposit
#write transaction to a python file
#while true
#input
#claassses 
#open()
#methods
#properties

class Bank:
    
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount
        
    def log_transaction(self,transaction_string):
            with open("transaction.txt", "a") as file:
                file.write(f"{transaction_string}\t\t\tBalance: {self.balance}\n")
        
    def withdrawl(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0    
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"withdraw {amount}")
        
    def deposit(self , amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0 
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"deposited {amount}")
            
account = Bank(15000)
while True:
    try:
        action = input("what kind of action you want to take: ")    
    except KeyboardInterrupt:
        print("\n leaving the atm \n")
        break
    if action in ["withdrawl", "deposit"]:
        if action == "withdrawl":
            amount = input("how much dou you want to take out ? ")
            account.withdrawl(amount)
        else:
            amount = input("how much do you want to put in ? ")     
            account.deposit(amount)
            
        print("your balance is : ",account.balance)
    else:
        print("that is not a valid option Try again")
