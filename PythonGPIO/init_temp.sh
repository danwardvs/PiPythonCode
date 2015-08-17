#!/bin/bash

echo "Getting you the names of connected thermometers..."


sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls