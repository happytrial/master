import unittest
import time
digits = open("ints.txt").readlines()
d = {}
for x in range(len(digits)):
    d["int{0}".format(x)] = int(digits[x].strip())
D_keys = list(d.keys())
D_values = list(d.values())

result = open("sum.txt").readlines()
time1 = open("time.txt").readlines()

class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual((D_values[0]+D_values[1]), int(result[0]))

    def test_time(self):
        self.assertEqual(time.ctime(time.time()), str(time1[0]))