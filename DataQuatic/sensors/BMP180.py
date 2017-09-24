#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Copyright 2017 Paul Barajas <paul.barajas@linux.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import Adafruit_BMP.BMP085 as BMP085

class BMP180:
    def __init__(self):
        self.sensor = BMP085.BMP085()

    @property
    def temperature(self):
        temp = self.sensor.read_temperature()
        return '{0:0.2f} *C'.format(temp)

    @property
    def presure(self):
        presure = self.sensor.read_pressure()
        return '{0:0.2f} Pa'.format(presure)

    @property
    def altitude(self):
        altitude = self.sensor.read_altitude()
        return '{0:0.2f} m'.format(altitude)
