#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime


def readcputemp():
    f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
    line = f.readline()
    f.close()
    cputemp = '%.1f' % (float(line) / 1000.0)
    return cputemp


def main():
    cputemp = readcputemp()
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    message = 'Raspberry Pi B+ cpu=' + cputemp + '℃ local time=' + timestamp
    print message


if __name__ == '__main__':
    main()
