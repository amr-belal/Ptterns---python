class Washing:
    def washing(self):
        print("start washing process")
    
class Rinsing:
    def rinsing(self):
        print("start rinsing process")
    
class Spinning:
    def spinning(self):    
        print("start spinning process")
    
class WashingMachine:
    def __init__(self):
        self.wash=Washing()
        self.rinse=Rinsing()
        self.spin=Spinning()
    def StartWashing(self):
        self.wash.washing()
        self.rinse.rinsing()
        self.spin.spinning()
        
obj=WashingMachine()
obj.StartWashing()

#================================================================================================

