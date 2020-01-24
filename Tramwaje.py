from timetable import Timetable
from table_times_source import table_times
from table_locations_source import table_locations

'''
The purpose of Tramwaje.py
is to create a class, which can simulate movement,
shows locations of an instance of a tram inside a line
and holds all records of a line - both stations and departures

'''

timetable = Timetable(table_times, table_locations, 100)


class Tram:
    """
    departures represent times when each line is departing
    stations are locations, which tram drives through
    """

    def __init__(self, name, departures, stations):
        self.name = name
        self.departures = departures
        self.stations = stations

    def get_departure(self, which_depart):
        # this allow to to get the value of a certain departure
        return self.departures[which_depart]

    def get_station(self, station_a):
        # this alllows to get the value of a certain station
        return self.stations[station_a]

    def show_location(self, departure_number, time):
        """
        Shows the location of a departure inside a line
        Given a certain time
        """
        # first time of the departure is a assign to a new integrer
        momentary_time = self.get_departure(departure_number)
        for counter, station in enumerate(self.stations[:-1]):
            # then the function looks through all the stations inside a line
            station_1 = self.get_station(counter)
            station_2 = self.get_station(counter+1)
            if(momentary_time <= time) and (time <= momentary_time + timetable.table[station_1][station_2]):
                # if it is before line reaches next station and after reaching previous station
                # the tram at the given moment must be between those stations
                location_1_x = timetable.table_location[station_1][0]
                location_1_y = timetable.table_location[station_1][1]
                location_2_x = timetable.table_location[station_2][0]
                location_2_y = timetable.table_location[station_2][1]
                time_delta = timetable.table[station_1][station_2]
                quotient = (time - momentary_time)/time_delta
                # from vector product there is an equation which shows a detailed location of a tram
                temp_x = location_1_x + \
                    (quotient*(location_2_x - location_1_x))
                temp_y = location_1_y + \
                    (quotient*(location_2_y - location_1_y))
                # in the end, the function returns those values
                return[temp_x, temp_y, station_1, station_2]
            else:
                # if it wasn't between those lines, the function has to keep on searching
                momentary_time = momentary_time + \
                    timetable.table[station_1][station_2]
        return None

    def show_timedelta(self, departure_number, time):
        starting_location = self.show_location(departure_number, time)
        ending_location = self.show_location(departure_number, time+1)
        # the tram is moving if locations on two separate occcasions are diffrent
        if (starting_location is not None) and (ending_location is not None):
            # if not, then the tram is not moving
            xspeed = (ending_location[0] - starting_location[0])
            yspeed = (starting_location[1] - ending_location[1])

            return [xspeed, yspeed]
        else:
            return None
