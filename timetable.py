'''
Class Timetable
shows timetable
shows timedelta
shows location of a stations
check is_conected


'''


class Timetable:
    """
    table represents timedelta between certain tram_stations
    table_location shows location of tram_stations on a canva in tkinter
    """

    def __init__(self, table, table_location, tram_stations):
        self.table = table
        self.tram_stations = tram_stations
        self.table_location = table_location

    def get_from_table(self, station_c, station_d):
        return self.table[station_c, station_d]
    """
    checks, whether certain stations are connected
    [] means that two stations aren't connected
    """

    def is_connected(self, station_a, station_b):
        if station_a == station_b:
            return False
        elif self.table[station_a][station_b] is []:
            return False
        else:
            return True
