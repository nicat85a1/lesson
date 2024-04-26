"""class TrafficLight:
    '''This is a traffic light class'''
    color = 'green'

    def action(self):
        print('Go')

print(TrafficLight.__doc__)"""

"""class TrafficLight:
    '''This is an updated traffic light class'''

    # Class variable
    traffic_light_address = 'NYC_Cranberry_Hicks'

    def __init__(self, color):

        # Instance variable assigned inside the class constructor
        self.color = color

    def action(self):
        if self.color=='red':

            # Instance variable assigned inside a class method
            self.next_color = 'yellow'
            print('Stop & wait')
        elif self.color=='yellow':
            self.next_color = 'green'
            print('Prepare to stop')
        elif self.color=='green':
            self.next_color = 'red'
            print('Go')
        else:
            self.next_color = 'Brandy'
            print('Stop drinking 😉')

# Creating class objects
for c in ['red', 'yellow', 'green', 'fuchsia']:
    c = TrafficLight(c)
    print(c.traffic_light_address)
    print(c.color)
    c.action()
    print(c.next_color)
    print('\n')"""

"""# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code"""