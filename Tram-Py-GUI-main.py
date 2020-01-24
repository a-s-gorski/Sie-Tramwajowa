from tkinter import *
import random
import time
from Tramwaje import Tram
from timetable import Timetable
from tkinter.ttk import *
from table_times_source import table_times
from table_locations_source import table_locations

"""
Data for testing - basic timetable and Tram

"""
timetable = Timetable(table_times, table_locations, 100)

tram_1 = Tram(1, (0, 20, 40, 60, 80, 100, 120, 140, 160, 180),
              (0, 1, 2, 3, 4, 5, 10, 15, 10, 5))
tram_2 = Tram(1, (5, 15, 25, 35, 45, 55, 65, 70, 80, 90), (4, 5, 6, 7, 8, 9))
tram_3 = Tram(1, (5, 15, 25, 35, 60, 70, 80, 90, 100, 110),
              (11, 12, 13, 14, 15, 16))
tram_4 = Tram(1, (5, 15, 25, 35, 55, 77, 88, 91, 94, 101),
              (21, 22, 23, 47, 63, 83))
tram_5 = Tram(1, (5, 15, 25, 35, 45, 55, 65, 75, 85, 95),
              (60, 61, 41, 42, 22, 21))
tram_6 = Tram(1, (5, 15, 25, 35, 40, 45, 50, 60, 65, 70),
              (33, 34, 54, 55, 54, 44, 43, 33))
tram_7 = Tram(1, (5, 15, 25, 35, 45, 50, 60, 70, 80, 90),
              (81, 82, 62, 41, 20, 0))
tram_8 = Tram(1, (5, 15, 25, 35, 45, 50, 55, 60, 65, 70, 75),
              (55, 56, 57, 58, 59, 60))
tram_9 = Tram(1, (5, 15, 25, 35, 50, 80, 100, 110,
                  120, 130), (72, 71, 70, 49, 28, 9))
tram_10 = Tram(1, (5, 15, 25, 35, 50, 60, 70, 80,
                   90, 120), (0, 20, 40, 41, 21, 1))

trams = [tram_1, tram_2, tram_3, tram_4, tram_5,
         tram_6, tram_7, tram_8, tram_9, tram_10]
tram_colors = ["navy", "light blue", "gold", "purple",
               "bisque2", "green2", "pink1", "yellow", "linen", "rosy brown"]


"""
It creates tkinter-window
"""
window = Tk()
window.title("Tram-Py")
window.geometry('1920x1080')

"""
Then let's create canvas

"""

canvas = Canvas(window, width=1920, height=1080, bg="azure")

canvas.pack()

"""
We create comboboxes to control user input
"""

combo_time_1 = Combobox(window, text="starting time")
combo_time_1.place(x=1700, y=800)
combo_time_2 = Combobox(window)
combo_time_2.place(x=1700, y=825)

description_1 = Label(window, text="simulation starting time :")
description_1.place(x=1550, y=800)

Info_time = Label(window, text="Current time")
Info_time.place(x=1700, y=850)

description_2 = Label(window, text="simulation ending time :")
description_2.place(x=1550, y=850)
combo_time_1['values'] = (0, 25, 50, 100, 150, 200)
combo_time_2['values'] = (0, 25, 50, 100, 150, 200)

"""
Checkbuttons to select trams
function iterates through all trams to create checkbuttons
for each one of them

"""

checkbuttons = {}


for i in range(len(trams)):
    checkbuttons[f"{i}"] = Checkbutton(window, text=f"{i}")
    checkbuttons[f"{i}"].place(x=1700, y=(500+(30*i)))
"""
If the button is clicked
Then data from combo_times is gathered
and from checkbuttons we find out, which trams user has selected
"""


def clicked():
    # if the button is clicked it gathers starting_time and ending_times from comboboxes
    starting_time = int(combo_time_1.get())
    ending_time = int(combo_time_2.get())
    trams_selected = []
    for counter, tram_iterated in enumerate(trams):
        if checkbuttons[f"{counter}"].instate(['selected']):
            trams_selected.append(tram_iterated)
    simulate_tram(starting_time, ending_time, trams_selected)


btn_trampy = Button(window, text="Tram-Py Simulate Network", command=clicked)

btn_trampy.place(x=1700, y=900)

"""
The purpose of this function is to create stations with locations from tram_locations_source.py
"""


def create_stations(timetable):
    for counter_location, location in enumerate(timetable.table_location):
        location_x = timetable.table_location[counter_location][0]
        location_y = timetable.table_location[counter_location][1]
        location_x_1 = location_x + 30
        location_y_1 = location_y + 30
        canvas.create_rectangle(location_x, location_y,
                                location_x_1, location_y_1, fill="red")


"""
time_label is used to control time display
"""

time_label = Label(window, text=None)
time_label.place(x=1700, y=875)

"""
This is a main function of a software:
it decapitetes the movement of a tram:
"""


def simulate_tram(starting_time, ending_time, tramways):
    # first the empty set for object, that are going to be animated
    animated_objects = []
    # then each dictionary correspondes with a line and each key will represent a tram (departure)
    for tram in tramways:
        animated_objects.append({})
    # we display stations and set time_label1
    create_stations(timetable)
    time_label['text'] = starting_time

    for counter_tram, tram in enumerate(tramways):
        # we assign tram to a currently edited tram_animate
        for counter_departures, departure in enumerate(tram.departures[:-1]):
            # for each departure before starting_time we check, whether there are trams, that are moving right now
            if(tram.get_departure(0) < starting_time) and (tram.show_location(i, starting_time) is not None):
                temprorary_location = tram.show_location(
                    counter_departures, starting_time)
                loc_x = temprorary_location[0]
                loc_y = temprorary_location[1]
                loc_x_1 = loc_x + 30
                loc_y_1 = loc_y + 30
                # if so, we place tram on a canva
                animated_objects[counter_tram][f"{counter_departures}"] = (canvas.create_rectangle(
                    loc_x, loc_y, loc_x_1, loc_y_1, fill=tram_colors[counter_tram1]))
    temp_time = starting_time
    # then we assing starting time to temp_time which we will be iterating through
    # to this place its alright
    while temp_time <= ending_time:
        for counter_tram, tram in enumerate(tramways):
            for departures_counter, departure in enumerate(tram.departures):
                # if the tram is departing RIGHT NOW we place a new instance on a canva
                if tram.get_departure(departures_counter) == temp_time:
                    temprorary_location = tram.show_location(
                        departures_counter, temp_time)
                    loc_x = temprorary_location[0]
                    loc_y = temprorary_location[1]
                    loc_x_1 = loc_x + 30
                    loc_y_1 = loc_y + 30
                    animated_objects[counter_tram][f"{departures_counter}"] = canvas.create_rectangle(
                        loc_x, loc_y, loc_x_1, loc_y_1, fill=tram_colors[counter_tram])
                if tram.show_timedelta(departures_counter, temp_time) is not None and tram.show_location(departures_counter, temp_time) is not None and f"{departures_counter}" in animated_objects[counter_tram]:
                    # if the tram is moving right now we have to move corresponging object on a canva
                    movement_speed = tram.show_timedelta(
                        departures_counter, temp_time)
                    move_x = movement_speed[0]
                    move_y = movement_speed[1] * (-1)
                    canvas.move(
                        animated_objects[counter_tram][f"{departures_counter}"], move_x, move_y)
        # after making all of the changes the window is updated
        window.update()
        time.sleep(0.1)
        temp_time = temp_time + 1
        time_label['text'] = temp_time
    # after the time is over, whole canvas is cleared to make space for a new simulation
    canvas.delete("all")
    create_stations(timetable)


if __name__ == "__main__":
    window.mainloop()
