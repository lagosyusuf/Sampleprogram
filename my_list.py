from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

toyota_camry = Car('Toyota', 'Camry', 32000, 275, 8)  # Use the named tuple to describe a car
honda_accord = Car('Honda', 'Accord', 37495, 305, 5)  # Use the named tuple to describe a different car

print(toyota_camry)
print(honda_accord)
print(toyota_camry.price)
