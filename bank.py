class bank:
    
    def __init__(self,owner,bal):
     self.owner=owner
     self.bal=bal
    
    def deposit(self,value):
     self.bal=self.bal+value
     print(self.bal)
     print(self.owner)
    
    def withdraw(self,value):
     if (self.value<=self.bal):
         self.bal=self.bal-self.value
         print("balance available")
         print(self.bal)
     else:
         print("insufficient funds")
         
         
ba=bank("divyam",50000)
ba.deposit(10000) 