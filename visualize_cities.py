# name: Kevin Lin
# date: 02/28/2021
# purpose: draw cities on world.png

from cs1lib import *

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360
SCALE = 2

time = 0
count = 0

# Parameters: file is the string name of a CSV file, count is an integer and is the number of lines considered
# Parameters: info is a number 1-3 corresponding to population,latitude,longitude respectively
# reads CSV files that go city_name,population,latitude,longitude per line and returns a list with specific information
def draw_list(file, count, info):
    list = []
    i = 0
    world_cities_r = open(file, "r")

    for line in world_cities_r:
        if count == i:
            break
        a = line.strip().split(",")
        list.append(float(a[info]))
        i = i + 1

    world_cities_r.close()
    return list

# draw "cities"/circles based off of the latitude and longitude lists
def draw_cities():
    lat = draw_list("txt files/cities_population.txt", 50, 2)
    long = draw_list("txt files/cities_population.txt", 50, 3)
    set_fill_color(0, 0, 0)
    for i in range(0, count):
        draw_circle((WINDOW_WIDTH / 2) + (long[i] * SCALE), (WINDOW_HEIGHT / 2) - (lat[i] * SCALE), 5)

# Parameters: max is an integer that will cap the value of count
# creates a 40 frame delay before adding another city to be drawn
def delay(max):
    global time, count
    if count == max:
        return

    if time == 40:
        time = 0
        count = count + 1

    time = time + 1

# final draw function
def main():
    img = load_image("Images/world.png")
    draw_image(img, 0, 0)
    delay(50)
    draw_cities()


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
