#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
from DataQuatic.sensors import BMP180

class TestSensors(unittest.TestCase):
    def __init__(self):
        self.bmp180 = BMP180.BMP180()

    def test_bmp180(self):
        self.assertTrue(self.bmp180.temperature)
        self.assertTrue(self.bmp180.pressure)
        self.assertTrue(self.bmp180.altitude)
