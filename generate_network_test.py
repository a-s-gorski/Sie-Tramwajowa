from generate_network import create_locations, create_timetable
import unittest
from random import uniform
"""
There are some basic unittests performed here

"""


class TestGenerateNetwork(unittest.TestCase):
    """
    class inherits from unittest.TestCase
    it requires assertEqual and assertLess
    """

    def test_timetable(self):
        # the purpose of test_timetable is to check if the timetable is symetrical
        # for each test there is "pseudorandomly" generated amount of iterations
        self.iterations_amount = int(uniform(10, 200))
        for test_length in range(self.iterations_amount):
            self.test_timetable = create_timetable(test_length)
            for starting_counter, starting_station in enumerate(self.test_timetable):
                for ending_counter, ending_station in enumerate(self.test_timetable):
                    """
                    The task of unittest is to check if corresponding stations have the same time_delta
                    """
                    first_value = self.test_timetable[starting_counter][ending_counter]
                    second_value = self.test_timetable[ending_counter][starting_counter]
                    self.assertEqual(first_value, second_value)

    def test_locations(self):
        """
        The purpose of this function is to check
        if tram_stations will fit on the canva in Tram-Py-Gui-Main
        """
        x_amount = int(uniform(1, 20))
        y_amount = int(uniform(1, 5))
        self.test_locations = create_locations(x_amount, y_amount)
        for location in self.test_locations:
            self.assertLess(location[0], 1920)
            self.assertLess(location[1], 1080)


if __name__ == '__main__':
    # begins running unittest
    unittest.main()
