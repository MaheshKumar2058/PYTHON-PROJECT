class Bikeshop:
    
    def __init__(self,stock):
        self.stock=stock
        
    def display_Bikes(self):
        print("Total Bikes", self.stock)
        
    def rentFor_Bike(self,q):
        
        if q<=0:
            print("Enter the positive value or greater than zerro")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total prices", q*1000)
            print("Total Bikes", self.stock)
            
obj = Bikeshop(100)
            
while True:
    uc=int(input('''
                 1 Display Stocks
                 2 Rent a Bike
                 3 Exit
                 '''))
     
    if uc == 1:
        obj.display_Bikes()
    elif uc == 2:
        n=int(input("enter the qty..."))
        obj.rentFor_Bike(n) 
    else:
        break