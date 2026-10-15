class BankAccount:
    bank_name="ABC Bank"
    account_numbers=set()
    total_accounts=0

    def __init__(self,owner,account_no,balance):
        if not BankAccount.account_no_check(account_no):
            raise ValueError("Invalid Account Number")
        if not BankAccount.balance_check(balance):
            raise ValueError("Invalid Balance Amount")
        if account_no in BankAccount.account_numbers:
            raise ValueError("Account Number already exists")
        BankAccount.account_numbers.add(account_no)
        self.owner=owner
        self.account_no=account_no
        self.__balance=balance
        BankAccount.total_accounts+=1
        
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls,new_bank_name):
        cls.bank_name=new_bank_name

    @staticmethod
    def account_no_check(account_no):
        return (isinstance(account_no,str) and len(account_no)==10 and account_no.isdigit() and not isinstance(account_no,bool))
    
    @staticmethod
    def balance_check(balance):
        return(isinstance(balance,(int,float)) and balance>=0 and not isinstance(balance,bool))
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if (not isinstance(amount,(int,float)) or isinstance(amount,bool) or amount<=0):
            print("Invalid deposit amount")
        else:
            self.__balance+=amount

    def withdrawal(self,amount):
        if(not isinstance(amount,(int,float)) or isinstance(amount,bool) or amount>self.__balance or amount<=0):
            print("Invalid withdrawal amount")
        else:
            self.__balance-=amount

    def __eq__ (self,other):
        if not isinstance(other,BankAccount):
            return NotImplemented
        return self.account_no==other.account_no
    
    def has_lower_balance_than(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __str__(self):
        return f"Owner Name: {self.owner}\nAccount Number: {self.account_no}\nBalance: {self.__balance}"
    
class SavingAccount(BankAccount):
    def __init__(self, owner, account_no, balance,interest_rate):
        if not SavingAccount.interest_rate_check(interest_rate):
            raise ValueError("Invalid interest rate")
        super().__init__(owner, account_no, balance)
        self.interest_rate=interest_rate

    @staticmethod
    def interest_rate_check(interest_rate):
        return (isinstance(interest_rate,(int,float)) and not isinstance(interest_rate,bool) and interest_rate>=0)
    
    def calculate_interest (self):
        interest=self.balance*(self.interest_rate/100)
        return interest
    
    def __str__(self):
        return f"{super().__str__()}\nInterest Earned: {self.calculate_interest()}"

b1 = BankAccount("Ali", "1234567890", 5000)
b2 = BankAccount("Ahmed", "2345678901", 3000)
s1 = SavingAccount("Sara", "3456789012", 10000, 5)

print("=== ACCOUNT DETAILS ===")
print(b1)
print(b2)
print(s1)

print("\n=== TRANSACTIONS ===")
b1.deposit(1000)
b1.withdrawal(500)
print("Balance after transactions:", b1.balance)

print("\n=== OOP FEATURES ===")
print("Are b1 and b2 equal?", b1 == b2)
print("Does b1 have a lower balance than s1?", b1.has_lower_balance_than(s1))
print("Interest earned by s1:", s1.calculate_interest())
print("Bank name:", BankAccount.get_bank_name())
BankAccount.set_bank_name("XYZ Bank")
print("Updated bank name:", BankAccount.get_bank_name())

print("\n=== ACCOUNT SUMMARY ===")
print("Total accounts:", BankAccount.total_accounts)