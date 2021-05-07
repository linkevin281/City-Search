# name: Kevin Lin
# date: 02/25/2021
# purpose: define city class

# Parameters:
# country_code is a two-letter string, name is a string, region is a two-character string
# pop is a positive integer, latitude is a float, longitude is a float
class City:
    def __init__(self, country_code, name, region, pop, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.pop = pop
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return str(self.name) + "," + str(self.pop) + "," + str(self.latitude) + "," + str(self.longitude)

