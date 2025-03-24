class BankAccount:
    def __init__(self,owner,balance=0):
    
         self.owner = owner
         self.balance = balance
    

    def deposit(self,amount):
         self.balance += amount 
         print(f"{amount} deposited. new amount: {self.balance}")
        
    def withdraw(self,amount):
         if amount > self.balance: 
            print(f"insuffient balance!")

         else: 
             self.balance -= amount 
             print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")  


account1 = BankAccount("Gedeon", 500)
account1.deposit(200)
account1.withdraw(100)
account1.check_balance()
   
         
       
        