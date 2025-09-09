zz = "##############################################"
print(zz)

aa = "For this challenge, create a bank account that has two attributes"
bb = "owner"
cc = "balance"

dd = "and has two methods"
ee = "deposit"
ff = "withdraw"

print(aa)
print(bb)
print(cc)
print(zz)
print(dd)
print(ee)
print(ff)
print(zz)

gg = "As an added requirement, withdrawals may not exceed the available balance"
hh = "Instantiate your class, make several deposits and withdrawls, and test to make sure the account can't be overdrawn"
print(gg)
print(hh)
print(zz)

class Account:
    pass
# Instantiate the class
acct1 = Account("Todd",100)

# Print the object
print(acct1)
print(zz)

# Show the account owner attribute
print(acct1.owner)
print(zz)

# Show the account balance attribute
print(acct1.balance)
print(zz)

# Make a series of deposits and withdrawals
print(acct1.deposit(50))

print(acct1.withdraw(75))
print(zz)

# Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))
print(zz)

# class Simple():
#    def __init__(self,value):
#        self.value = value
#    def add_to_value(self,amount):
#        self.value = self.value + amount