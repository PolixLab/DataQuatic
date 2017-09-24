#/bin/bash

#script to install dependencies for BMP180 sensor

#author: Paul Barajas <paul.barajas@linux.com>
#Usage: Execute the script without argument
#Note: Make sure that you have python 3 installed and your 
#git account configured in your OS.

git clone https://github.com/adafruit/Adafruit_Python_BMP.git
python3 Adafruit_Python_BMP/setup.py install
rm -r Adafruit_Python_BMP
