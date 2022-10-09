from Car import Car

car_1 = Car("Peugeot", "206", 2008, "gray")
car_2 = Car("Ford", "Fiesta", 2016, "black")

#Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

car_1.info()
car_1.drive()
car_2.stop()