"""class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)"""

"""class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())"""

"""class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)"""

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())"""

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in type()
print(type(School_bus))"""

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))"""

"""import random

class flashcard:
	def __init__(self):
	
		self.fruits={'apple':'red',
					'orange':'orange',
					'watermelon':'green',
					'banana':'yellow'}
		
	def quiz(self):
		while (True):
		
			fruit, color = random.choice(list(self.fruits.items()))
			
			print("What is the color of {}".format(fruit))
			user_answer = input()
			
			if(user_answer.lower() == color):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("enter 0 , if you want to play again : "))
			if (option):
				break

print("welcome to fruit quiz ")
fc=flashcard()
fc.quiz()"""

"""# Import required modules
from random import shuffle


# Define a class to create
# all type of cards
class Cards:
	global suites, values
	suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

	def __init__(self):
		pass


# Define a class to categorize each card
class Deck(Cards):
	def __init__(self):
		Cards.__init__(self)
		self.mycardset = []
		for n in suites:
			for c in values:
				self.mycardset.append((c)+" "+"of"+" "+n)

	# Method to remove a card from the deck
	def popCard(self):
		if len(self.mycardset) == 0:
			return "NO CARDS CAN BE POPPED FURTHER"
		else:
			cardpopped = self.mycardset.pop()
			print("Card removed is", cardpopped)


# Define a class gto shuffle the deck of cards
class ShuffleCards(Deck):

	# Constructor
	def __init__(self):
		Deck.__init__(self)

	# Method to shuffle cards
	def shuffle(self):
		if len(self.mycardset) < 52:
			print("cannot shuffle the cards")
		else:
			shuffle(self.mycardset)
			return self.mycardset

	# Method to remove a card from the deck
	def popCard(self):
		if len(self.mycardset) == 0:
			return "NO CARDS CAN BE POPPED FURTHER"
		else:
			cardpopped = self.mycardset.pop()
			return (cardpopped)


# Driver Code
# Creating objects
objCards = Cards()
objDeck = Deck()

# Player 1
player1Cards = objDeck.mycardset
print('\n Player 1 Cards: \n', player1Cards)

# Creating object
objShuffleCards = ShuffleCards()

# Player 2
player2Cards = objShuffleCards.shuffle()
print('\n Player 2 Cards: \n', player2Cards)

# Remove some cards
print('\n Removing a card from the deck:', objShuffleCards.popCard())
print('\n Removing another card from the deck:', objShuffleCards.popCard())"""

if 0 == True:
    print("True")
else:
    print("False")

if 1 == True:
    print("True")
else:
    print("False")

if -1 == True:
    print("True")
else:
    print("False")