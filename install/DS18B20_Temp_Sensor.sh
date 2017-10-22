#/bin/bash

#script to install dependencies for DS18B20 Temperature Sensor

#author: Erick Noriega <e2@live.com.mx>
#Usage: Execute the script without argument
#Note: Make sure that you have python 3 installed and your
#git account configured in your OS.

rm -rf DS18B20
git clone ssh://ericknoriega@review.gerrithub.io:29418/PolixLab/DS18B20

cd DS18B20/src/
make
make test
cd ../..
mkdir -p bin
cp -r DS18B20/src/libDS18B20.so* bin
cp DS18B20/src/dstest bin/DS18B20bin
rm -rf DS18B20
