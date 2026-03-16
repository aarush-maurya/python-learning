#Abstraction is a pillar of OOP, which just means you hide the internal logic when you call a class method
class Car:
    acc = False
    brk = False
    clutch = False
    
    def __init__(self, acc, brk, clutch):
        self.acc = acc
        self.brk = brk
        self.clutch = clutch
        
    def start(self):
        self.acc = True
        self.brk = True
        self.brk = False
        print(f"The car has been started....")
        
car = Car(False, False, False)
car.start() # The car has been started....

#In the above example, you can see when we call car.start() it prints the strin "The car has been started...." 
# But it doesnt show the logic running inside i.e the acc and clutch set to True
