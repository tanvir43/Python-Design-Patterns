class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    #Mutator method or setter method i.e setter method is considered as a Mutator method when a class deals with private attribute(self__balance)
    def deposit(self, amount):
        print("old balance", self.__balance)
        self.__balance += amount
        print("new balance", self.__balance)
        return self.__balance

    #Another Mutator method
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Error: amount {amount} exceeds your current balance {self.__balance}")
        self.__balance -= amount
        return self.__balance
    
    #Accessor method or getter method, we use this method to access our private class attribute(self.__balance)
    def get_balance(self):
        return self.__balance

account = BankAccount(2000)

"""
Can not access class attribute '__balance', 
we restricted it to be accessed from outside of the class
by using '__''
"""
#print(f"account balance {account.__balance}") # will raise an error

print(f"Deposit amount 1000 {account.deposit(1000)}")
print(f"Withdraw amount 500 {account.withdraw(500)}")
print(f"Now balance is {account.get_balance()}")        
