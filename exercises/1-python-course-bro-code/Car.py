class Car:

    wheels = 4 #class variable

    def __init__(self,make,model,year,color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable

    def info(self):
        print("Make: ", self.make, "\nModel: ", self.model, "\nYear: ", self.year, "\nColor: ", self.color)

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")