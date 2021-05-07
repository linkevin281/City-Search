# name: Kevin Lin
# date: 02/25/2021
# purpose: output cities_out.txt

from City import City
from string import *

cities = []

# creates a list of city objects according to world_cities.txt
def create_cities():
    world_cities_r = open("txt files/world_cities.txt", "r")

    for line in world_cities_r:
        a = line.strip().split(",")
        cities.append(City(str(a[0]), str(a[1]), str(a[2]), int(a[3]), float(a[4]), float(a[5])))

    world_cities_r.close()

# writes CSV file cities_out.txt with each line containing a city's information
# city name,population,latitude,longitude
def write_output():
    world_cities_w = open("txt files/cities_out.txt", "w")

    for i in range(0, len(cities)):

        world_cities_w.write(str(cities[i]) + "\n")

    world_cities_w.close()

# Parameters: the_list is a list, p and r are integers representing list indices of the_list, and p is less than r
# compare_func is a function
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]

    while True:
        if j == r:
            the_list[r], the_list[i+1] = the_list[i+1], the_list[r]
            return i+1

        elif not compare_func(the_list[j], pivot):
            j = j + 1

        elif compare_func(the_list[j], pivot):
            i = i + 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            j = j + 1

def quicksort(the_list, p, r, compare_func):
    if r < p + 1:
        return

    quicksort(the_list, p, partition(the_list, p, r, compare_func)-1, compare_func)
    quicksort(the_list, partition(the_list, p, r, compare_func)+1, r, compare_func)

def sort(the_list, compare_func):
    pass


# Parameters: both a and b are ints
# returns true if a is less than b or equal, false if a is greater
def compare_int(a, b):
    return a <= b

# Parameters: Both a and b are strings
# returns true if a is less than b in ASCII without caps or equal, false if a is greater
def compare_string(a, b):
    return a.lower() <= b.lower()

# create_cities()
# write_output()


list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quicksort(list, 0, 8, compare_int)
print(list)
