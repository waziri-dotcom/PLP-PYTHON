class Vehicle:
    def move(self):
        print("This vehicle moves 🚙")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water!")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    v.move()
