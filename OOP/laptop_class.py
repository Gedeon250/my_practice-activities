class Laptops:
    def __init__(self, HardDisk, Architecture, Model):  # Fixed constructor
        self.HardDisk = HardDisk
        self.Architecture = Architecture
        self.Model = Model
        
    def Turnon(self): 
        print("This Laptop can turn on by pressing the power button")
    
    def bits(self):
        print("This type might support a few software applications")


