# name: Kevin Lin
# date: 02/28/2021
# purpose: create cities_alpha.txt, cities_population.txt, cities_latitude.txt

from City import City
from quicksort import sort

cities = []

# creates a list of city objects according to world_cities.txt
def create_cities():
    world_cities_r = open("txt files/world_cities.txt", "r")

    for line in world_cities_r:
        a = line.strip().split(",")
        cities.append(City(str(a[0]), str(a[1]), str(a[2]), int(a[3]), float(a[4]), float(a[5])))

    world_cities_r.close()

# Parameter: file is the name of a .txt file to be written on
# writes CSV file cities_out.txt with each line containing a city's information
# city name,population,latitude,longitude
def write_output(file):
    world_cities_w = open(file, "w")

    for i in range(0, len(cities)):
        world_cities_w.write(str(cities[i]) + "\n")

    world_cities_w.close()

# Parameters: Both a and b are strings
# compares the ACSII values of two a and b and returns false if a is greater, else true
def compare_alpha(a, b):
    return a.name <= b.name

# Parameters: both a and b are floats
# returns false if a is less than b, else true
def compare_pop(a, b):
    return a.pop >= b.pop

# Parameters: both a and b are floats
# returns false if a is greater than b, else true
def compare_latitude(a, b):
    return a.latitude <= b.latitude

# Parameters: the_list is a list of city objects, compare_func is a function
# sorts the_list alphabetically A-Z and writes the output in cities_alpha.txt
def sort_alpha(the_list, compare_func):
    sort(the_list, compare_func)
    write_output("txt files/cities_alpha.txt")

# Parameters: the_list is a list of city objects, compare_func is a function
# sorts the_list by descending population and writes the output in cities_population.txt
def sort_population(the_list, compare_func):
    sort(the_list, compare_func)
    write_output("txt files/cities_population.txt")

# Parameters: the_list is a list of city objects, compare_func is a function
# sorts the_list by increasing latitude and writes the output in cities_latitude.txt
def sort_latitude(the_list, compare_func):
    sort(the_list, compare_func)
    write_output("txt files/cities_latitude.txt")


create_cities()
sort_population(cities, compare_pop)
sort_alpha(cities, compare_alpha)
sort_latitude(cities, compare_latitude)