# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"


# Child class (inheritance + encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, battery, storage):
        super().__init__(brand, model)  # call parent constructor
        self.__battery = battery        # private attribute (encapsulation)
        self.storage = storage

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"🔋 Battery charged to {self.__battery}%")

    def use(self, hours):
        self.__battery = max(0, self.__battery - (hours * 10))
        print(f"📱 Used for {hours}h, battery now {self.__battery}%")

    def get_battery(self):  # getter
        return self.__battery


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 80, "256GB")
phone2 = Smartphone("Samsung", "Galaxy S23", 50, "128GB")

print(phone1.info())  # Apple iPhone 15
phone1.use(3)         # battery reduces
phone1.charge(20)     # battery increases
print("Battery left:", phone1.get_battery(), "%")
