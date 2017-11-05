# Copyright 2017 Erick Noriega <e2@live.com.mx>

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

import fnmatch
import os


class DS18B20:
    def __init__(self):
        print('running')
        for file in os.listdir('/sys/bus/w1/devices'):
            if fnmatch.fnmatch(file, '28-*'):
                self.sensor=file

    @property
    def temperature(self):
        temp = 50.3
        return '{0:0.2f} *C'.format(temp)

def main():
    instance = DS18B20()
    print(instance.sensor)
    print(instance.temperature)
if __name__ == "__main__": main()
