from random import uniform
"""
This file is not necessary for the software to funcionate, but I used it to show, how I created
table_time_source.py and table_locations_source.py
"""

file_times = open("table_times_source.py", "w+")

file_locations = open("table_locations_source.py", "w+")



"""
I create a loop which first creates an empty list for all the tram stations
then to each single one i assign random timein range(7, 15)
"""


def create_timetable(tram_stations):
    table_times = []
    for i in range(tram_stations):
        table_times.append([[]])
        for j in range(tram_stations):
            table_times[i].append([])

    for i in range(tram_stations):
        j = i + 1
        while j < tram_stations:
            table_times[i][j] = int(uniform(7, 15))
            table_times[j][i] = table_times[i][j]
            j = j + 1
    return table_times

"""
The second loop is used to assign locations on a canvas,
right now stations are placed on a grid 5x20
"""


def create_locations(x_coordinate, y_coordinate):
    table_locations = []
    i = 1
    while i <= x_coordinate:
        j = 1
        while j <= y_coordinate:
            location_x = 75 * i
            location_y = 150 * j
            j = j + 1
            table_locations.append([location_x, location_y])
        i = i + 1
    return table_locations


table_times_example = create_timetable(100)
table_locations_example = create_locations(20, 5)

"""
Finally i write those values in new files
"""

file_times.write("table_times = " + str(table_times_example))
file_locations.write("table_locations = " + str(table_locations_example))
