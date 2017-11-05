#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
from DataQuatic.sensors import BMP180, DS18B20

class TestSensors(unittest.TestCase):
    def __init__(self):
        self.bmp180 = BMP180.BMP180()
        instance = DS18B20()
    def test_bmp180(self):
        self.assertTrue(self.bmp180.temperature)
        self.assertTrue(self.bmp180.pressure)
        self.assertTrue(self.bmp180.altitude)

    def test_ds18b20(self):
        self.assertTrue(self.DS18B20.temperature)
