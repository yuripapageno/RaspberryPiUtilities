#!/bin/sh
cat /sys/class/thermal/thermal_zone0/temp | awk '{printf("%.1f\n", ($1=$1 / 1000))}'
