# name: Kevin Lin
# date: 03/01/2021
# purpose: define city class

# Parameters:
# name is a string, pop is a positive integer, latitude is a float, longitude is a float
class City:
    def __init__(self, name, pop, latitude, longitude):
        self.name = name
        self.pop = pop
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return str(self.name) + "," + str(self.pop) + "," + str(self.latitude) + "," + str(self.longitude)

