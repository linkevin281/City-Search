# name: Kevin Lin
# date: 02/28/2021
# purpose: create a city visual

from cs1lib import *
from City_extra import City


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360
SCALE = 2

ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NAME = []
POP = []
LAT = []
LONG = []
KEY1 = "1"
KEY2 = "2"
KEY3 = "3"
KEY4 = "4"
KEY0 = "0"
KEYA = "a"
KEYB = "b"
KEYC = "c"
KEYD = "d"
KEYE = "e"
KEYF = "f"
KEYG = "g"
KEYH = "h"
KEYI = "i"
KEYJ = "j"
KEYK = "k"
KEYL = "l"
KEYM = "m"
KEYN = "n"
KEYO = "o"
KEYP = "p"
KEYQ = "q"
KEYR = "r"
KEYS = "s"
KEYT = "t"
KEYU = "u"
KEYV = "v"
KEYW = "w"
KEYX = "x"
KEYY = "y"
KEYZ = "z"
KEY_SPACE = " "
KEY_EQUAL = "="

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed0 = False
presseda = False
pressedb = False
pressedc = False
pressedd = False
pressede = False
pressedf = False
pressedg = False
pressedh = False
pressedi = False
pressedj = False
pressedk = False
pressedl = False
pressedm = False
pressedn = False
pressedo = False
pressedp = False
pressedq = False
pressedr = False
presseds = False
pressedt = False
pressedu = False
pressedv = False
pressedw = False
pressedx = False
pressedy = False
pressedz = False
pressed_space = False
pressed_equal = False

time = 0
count = 0
count1 = 0
location = 0

r = 0
b = 0
g = 0

start = False
counter = False
start_search = False
check1 = False
check2 = False
search_display = False
legacy = False
search_mode = False

selection = ""
target = ""
search = ""
search_str = ""
string = ""
string2 = ""
search_list = []
cities = []

def key_down(key): # checks if a key is pressed
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal

    if key == KEY1:
        pressed1 = True
    if key == KEY2:
        pressed2 = True
    if key == KEY3:
        pressed3 = True
    if key == KEY4:
        pressed4 = True
    if key == KEY0:
        pressed0 = True
    if key == KEYA:
        presseda = True
    if key == KEYB:
        pressedb = True
    if key == KEYC:
        pressedc = True
    if key == KEYD:
        pressedd = True
    if key == KEYE:
        pressede = True
    if key == KEYF:
        pressedf = True
    if key == KEYG:
        pressedg = True
    if key == KEYH:
        pressedh = True
    if key == KEYI:
        pressedi = True
    if key == KEYJ:
        pressedj = True
    if key == KEYK:
        pressedk = True
    if key == KEYL:
        pressedl = True
    if key == KEYM:
        pressedm = True
    if key == KEYN:
        pressedn = True
    if key == KEYO:
        pressedo = True
    if key == KEYP:
        pressedp = True
    if key == KEYQ:
        pressedq = True
    if key == KEYR:
        pressedr = True
    if key == KEYS:
        presseds = True
    if key == KEYT:
        pressedt = True
    if key == KEYU:
        pressedu = True
    if key == KEYV:
        pressedv = True
    if key == KEYW:
        pressedw = True
    if key == KEYX:
        pressedx = True
    if key == KEYY:
        pressedy = True
    if key == KEYZ:
        pressedz = True
    if key == KEY_SPACE:
        pressed_space = True
    if key == KEY_EQUAL:
        pressed_equal = True


def key_up(key): # checks if a key is released
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal

    if key == KEY1:
        pressed1 = False
    if key == KEY2:
        pressed2 = False
    if key == KEY3:
        pressed3 = False
    if key == KEY4:
        pressed4 = False
    if key == KEY0:
        pressed0 = False
    if key == KEYA:
        presseda = False
    if key == KEYB:
        pressedb = False
    if key == KEYC:
        pressedc = False
    if key == KEYD:
        pressedd = False
    if key == KEYE:
        pressede = False
    if key == KEYF:
        pressedf = False
    if key == KEYG:
        pressedg = False
    if key == KEYH:
        pressedh = False
    if key == KEYI:
        pressedi = False
    if key == KEYJ:
        pressedj = False
    if key == KEYK:
        pressedk = False
    if key == KEYL:
        pressedl = False
    if key == KEYM:
        pressedm = False
    if key == KEYN:
        pressedn = False
    if key == KEYO:
        pressedo = False
    if key == KEYP:
        pressedp = False
    if key == KEYQ:
        pressedq = False
    if key == KEYR:
        pressedr = False
    if key == KEYS:
        presseds = False
    if key == KEYT:
        pressedt = False
    if key == KEYU:
        pressedu = False
    if key == KEYV:
        pressedv = False
    if key == KEYW:
        pressedw = False
    if key == KEYX:
        pressedx = False
    if key == KEYY:
        pressedy = False
    if key == KEYZ:
        pressedz = False
    if key == KEY_SPACE:
        pressed_space = False
    if key == KEY_EQUAL:
        pressed_equal = False

# creates a list of city objects according to world_cities.txt
def create_cities():
    world_cities_r = open("txt files/cities_alpha_extra.txt", "r")

    for line in world_cities_r:
        a = line.strip().split(",")
        cities.append(City(str(a[0]), int(a[1]), float(a[2]), float(a[3])))

    world_cities_r.close()

# generates lists with corresponding information
def generate_info_list():
    global NAME, POP, LAT, LONG
    for i in range(0, len(cities)):
        NAME.append(cities[i].name)
        POP.append(cities[i].pop)
        LAT.append(cities[i].latitude)
        LONG.append(cities[i].longitude)

# Parameters: file is the string name of a CSV file, count is an integer and is the number of lines considered
# Parameters: info is a number 1-4 corresponding to population,latitude,longitude,image respectively
# reads CSV files that go city_name,population,latitude,longitude,image per line and returns
# a list with specific information
def draw_list(file, count, info):
    list = []
    i = 0
    world_cities_r = open(file, "r")

    for line in world_cities_r:
        if count == i:
            break
        a = line.strip().split(",")
        list.append(a[info])
        i = i + 1

    world_cities_r.close()
    return list

# draw "cities"/circles based off of the latitude and longitude lists
def draw_cities():
    lat = draw_list("txt files/cities_population_extra.txt", 50, 2)
    long = draw_list("txt files/cities_population_extra.txt", 50, 3)
    set_fill_color(0, 0, 0)
    for i in range(0, count):
        draw_circle((WINDOW_WIDTH / 2) + (float(long[i]) * SCALE), (WINDOW_HEIGHT / 2) - (float(lat[i]) * SCALE), 5)

# Parameters: max is an integer that will cap the value of count
# creates a 40 frame delay before adding another city to be drawn
def delay_legacy(max):
    global time, count
    if count == max:
        return

    if time == 40:
        time = 0
        count = count + 1

    time = time + 1

# final draw function
def main_legacy():
    img = load_image("Images/world.png")
    draw_image(img, 0, 0)
    delay_legacy(50)
    draw_cities()

# creates a 40 frame delay and flips counter to true
def delay():
    global time, counter
    counter = False

    if time == 40:
        time = 0
        counter = True

    time = time + 1

# draws the background image
def draw_background():
    img = load_image("Images/world.png")
    draw_image(img, 0, 0)

# combines the main menu functions and runs them
def main_menu():

    main_menu_draw()
    main_menu_space()
    main_menu_delay()
    main_menu_functionality()

# draws the main_menu screen
def main_menu_draw():
    global count

    name = draw_list("txt files/cities_menu.txt", 10, 0)     # creates lists from cities_menu.txt
    population = draw_list("txt files/cities_menu.txt", 10, 1)
    lat = draw_list("txt files/cities_menu.txt", 10, 2)
    long = draw_list("txt files/cities_menu.txt", 10, 3)
    image = draw_list('txt files/cities_menu.txt', 10, 4)
    x = (WINDOW_WIDTH / 2) + (float(long[count]) * SCALE)
    y = (WINDOW_HEIGHT / 2) - (float(lat[count]) * SCALE)

    set_stroke_color(0, 0, 0)
    set_font_italic()
    set_font_bold()
    set_font_size(30)
    draw_text("The City Search Program", 145, 35)

    img = load_image(image[count])  # draws the city image + city dot + city information + supporting text
    set_fill_color(1, 0, 0)
    draw_circle(x, y, 5)
    draw_image(img, x - 150, y + 20)
    set_font_size(10)
    set_font_normal()
    set_font_bold()
    draw_text("Name: ", x - 50, y + 30)
    draw_text(name[count], x + 30, y + 30)
    draw_text("Population: ", x - 50, y + 50)
    draw_text(population[count], x + 30, y + 50)
    draw_text("Latitude: ", x - 50, y + 70)
    draw_text(lat[count], x + 30, y + 70)
    draw_text("Longitude: ", x - 50, y + 90)
    draw_text(long[count], x + 30, y + 90)

# draws the space bar and makes it pulse
def main_menu_space():
    global r, g, b
    set_font_italic()
    set_font_bold()
    set_font_size(20)
    set_stroke_color(r, g, b)
    r = r + 0.02
    g = g + 0.02
    b = b + 0.02
    if r > 1:
        r = 0
        g = 0
        b = 0
    draw_text("Press Space to Continue", 210, 350)

# creates a 2 second delay between swapping cities
def main_menu_delay():
    global count, count1, counter
    if counter:
        count1 = count1 + 1
    if count1 == 2:
        count = count + 1
        count1 = 0
    if count == 10:
        count = 0

# if space gets pressed on the menu continue to the search
def main_menu_functionality():
    global pressed_space, start
    if pressed_space:
        start = True

# main combination function for searches
def search_main():
    global start_search, check1, search_list, search_display

    if not start_search:
        search_draw()
        search_letter()
    if start_search:
        run_search()
        search_draw()
        result_parameters()
        search_results()
        result_functionality()
        if pressed_space:
            start_search = False
            check1 = False
    if search_display:
        draw_target()
        if pressed_space:
            start_search = False
            check1 = False
            search_display = False

# draws the initial search (place where you type)
def search_draw():
    global search_list, search_str, string, start_search

    if not start_search:
        set_stroke_color(0, 0, 0)
        set_font_normal()
        set_font_bold()
        set_font_size(25)
        draw_text("Enter City Name: ", 215, 100)

        set_font_normal()
        set_font_size(18)
        draw_text("Press zero for backspace", 10, 20)
        draw_text("Press equal for enter", 10, 45)

        string = search_str.join(search_list)
        set_stroke_color(0, 0, 0)
        set_font_normal()
        set_font_bold()
        set_font_size(15)
        draw_text(string, 150, 160)

        set_fill_color(0, 0, 0)
        draw_rectangle(145, 165, 430, 5)
        draw_line(148, 165, 148, 150)

        # draws the prelim search
        set_stroke_color(.66, .2, .2)
        draw_text("Did you mean: ", 140, 300)
        set_stroke_color(0, 0, 0)
        draw_text(str(cities[temp_search()].name), 290, 302)

# does a preliminary search and returns the index of the first city that matches
def temp_search():
    global string
    for i in range(0, len(cities)):
        if string <= cities[i].name.lower():
            return i

# runs the search and identifies the first city that is greater than or equal to the search string
def run_search():
    global string, target, check1
    if not check1:
        for i in range(0, len(cities)):
            if string <= cities[i].name.lower():
                target = i
                check1 = True
                break


# draws the search results
def search_results():
    global target, start_search, string2
    city1 = False
    city2 = False
    city3 = False
    city4 = False

    if start_search:
        set_stroke_color(0, 0, 0)
        set_font_normal()
        set_font_bold()
        set_font_size(15)
        draw_text("Search City: ", 0, 20)
        draw_text(string, 150, 20)

        set_stroke_color(0, 0, 0)
        set_font_normal()
        set_font_size(20)

        # cities that are drawn must be below the string2 value
        # finds the next 4 cities that are still within search parameters
        if cities[target].name.lower() < string2:
            draw_text(cities[target].name, 250, 60)
            draw_text("Press 1 to see: ", 20, 60)
            city1 = True
        if cities[target+1].name.lower() < string2:
            draw_text(cities[target+1].name, 250, 130)
            draw_text("Press 2 to see: ", 20, 130)
            city2 = True
        if cities[target+2].name.lower() < string2:
            draw_text(cities[target+2].name, 250, 200)
            draw_text("Press 3 to see: ", 20, 200)
            city3 = True
        if cities[target+3].name.lower() < string2:
            draw_text(cities[target+3].name, 250, 270)
            draw_text("Press 4 to see: ", 20, 270)
            city4 = True

        # if all searches fail then display no results
        if not city1 and not city2 and not city3 and not city4:
            set_font_size(25)
            draw_text("No Results!", 280, 100)
            draw_text("Are you sure you didn't have spaces?", 110, 150)

        return_space()

# creates a string2 to act as an upper limit for the search results
# does this by appending the next letter to the last letter of search string
# say search is "new", itll make string2 "nex" or if search is "zez" then string 2 is "zez " (with a space)
def result_parameters():
    global target, string2, string, ALPHA

    list1 = list(string)
    for i in range(0, len(ALPHA)):
        if ALPHA[i] == "z" and list1[len(list1)-1] == "z":
            list1.append(" ")

        elif ALPHA[i] == list1[len(list1) - 1]:
            list1[len(list1)-1] = ALPHA[i+1]


    string2 = "".join(list1)

# creates functionality for the 1-4 buttons in the display search results screen
def result_functionality():
    global pressed1, pressed2, pressed3, pressed4, selection, target, search_display
    if pressed1:
        selection = target
        search_display = True

    if pressed2:
        selection = target + 1
        search_display = True

    if pressed3:
        selection = target + 2
        search_display = True

    if pressed4:
        selection = target + 3
        search_display = True

# draws the selected city chosen
def draw_target():
    global NAME, POP, LAT, LONG, selection
    draw_background()

    x = (WINDOW_WIDTH / 2) + (float(LONG[selection]) * SCALE)
    y = (WINDOW_HEIGHT / 2) - (float(LAT[selection]) * SCALE)

    set_fill_color(1, 0, 0)
    draw_circle(x, y, 5)

    set_font_size(10)
    set_font_normal()
    set_font_bold()
    set_stroke_color(0, 0, 0)
    draw_text("Name: ", x - 80, y + 30)
    draw_text(str(NAME[int(selection)]), x, y + 30)
    draw_text("Population: ", x - 80, y + 50)
    draw_text(str(POP[int(selection)]), x, y + 50)
    draw_text("Latitude: ", x - 80, y + 70)
    draw_text(str(LAT[int(selection)]), x, y + 70)
    draw_text("Longitude: ", x - 80, y + 90)
    draw_text(str(LONG[int(selection)]), x, y + 90)

    set_font_size(20)
    set_font_bold()
    draw_text("Press 1-4 to cycle between cities!", 160, 20)

    return_space()

# draws the space bar and makes it pulse
def return_space():
    global r, g, b
    set_font_italic()
    set_font_bold()
    set_font_size(20)
    set_stroke_color(r, g, b)
    r = r + 0.02
    g = g + 0.02
    b = b + 0.02
    if r > 1:
        r = 0
        g = 0
        b = 0
    draw_text("Press Space to Return", 215, 350)

# when a button is pressed then add it to the search_list
def search_letter():
    global presseda, pressedb, pressedc, pressedd, pressede, pressedf, pressedg, pressedh, pressedi, pressedj, pressedk
    global pressedl, pressedm, pressedn, pressedo, pressedp, pressedq, pressedr, presseds, pressedt, pressedu, pressedv
    global pressedw, pressedx, pressedy, pressedz, pressed_space, pressed1, pressed2, pressed3, pressed4, pressed0
    global pressed_equal, start_search

    if presseda:
        search_list.append("a")
        presseda = False
    if pressedb:
        search_list.append("b")
        pressedb = False
    if pressedc:
        search_list.append("c")
        pressedc = False
    if pressedd:
        search_list.append("d")
        pressedd = False
    if pressede:
        search_list.append("e")
        pressede = False
    if pressedf:
        search_list.append("f")
        pressedf = False
    if pressedg:
        search_list.append("g")
        pressedg = False
    if pressedh:
        search_list.append("h")
        pressedh = False
    if pressedi:
        search_list.append("i")
        pressedi = False
    if pressedj:
        search_list.append("j")
        pressedj = False
    if pressedk:
        search_list.append("k")
        pressedk = False
    if pressedl:
        search_list.append("l")
        pressedl = False
    if pressedm:
        search_list.append("m")
        pressedm = False
    if pressedn:
        search_list.append("n")
        pressedn = False
    if pressedo:
        search_list.append("o")
        pressedo = False
    if pressedp:
        search_list.append("p")
        pressedp = False
    if pressedq:
        search_list.append("q")
        pressedq = False
    if pressedr:
        search_list.append("r")
        pressedr = False
    if presseds:
        search_list.append("s")
        presseds = False
    if pressedt:
        search_list.append("t")
        pressedt = False
    if pressedu:
        search_list.append("u")
        pressedu = False
    if pressedv:
        search_list.append("v")
        pressedv = False
    if pressedw:
        search_list.append("w")
        pressedw = False
    if pressedx:
        search_list.append("x")
        pressedx = False
    if pressedy:
        search_list.append("y")
        pressedy = False
    if pressedz:
        search_list.append("z")
        pressedz = False
    if pressed_space:
        search_list.append(" ")
        pressed_space = False
    if pressed0:
        if search_list:
            search_list.pop()
        pressed0 = False
    if pressed_equal:
        start_search = True

# lets you choose between the base lab or search
def legacy_or_search():
    global pressed1, pressed2, legacy, search_mode

    if not legacy or not search_mode:
        set_stroke_color(0, 0, 0)

        draw_text("For base Lab3 press 1", 200, 200)
        draw_text("For City Search press 2", 200, 250)

        if pressed1:
            legacy = True

        if pressed2:
            search_mode = True


# final draw function
def main():
    global start

    if not start:
        draw_background()
        delay()
        main_menu()

    if start:
        draw_background()
        legacy_or_search()

        if legacy:
            draw_background()
            delay_legacy(50)
            draw_cities()

        if search_mode:
            set_clear_color(1, 1, 1)
            clear()
            search_main()


create_cities()
generate_info_list()

start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, key_press=key_down, key_release=key_up)
