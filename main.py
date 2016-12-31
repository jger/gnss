#!/usr/bin/env python
import serial
import pynmea2
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--raw", help="raw output", action="store_true")
args = parser.parse_args()
if args.raw:
    print "raw turned on"
    raw=1 
else:
    raw=0

ser1 = serial.Serial( 
#   port='/dev/ttyAMA0',
#   port='/dev/ttyS0',
    port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AE01F64S-if00-port0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser2 = serial.Serial(
#   port='/dev/ttyAMA0',
#   port='/dev/ttyS0',
    port='/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AH01CFIG-if00-port0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def parseGPS(str,ser):
    if str.find('GGA') > 0:
       msg = pynmea2.parse(str)
       print '<',ser,'> ', 
       print "Timestamp: %s -- Lat: %s  -- Lon: %s  -- Altitude: %s %s" % (msg.timestamp,"{:<15}".format(msg.latitude),"{:<15}".format(msg.longitude),msg.altitude,msg.altitude_units)

def rawGPS(str,ser):
       print '<',ser,'> ',str,


while 1:
    x=ser1.readline()
    if raw==0: 
	parseGPS(x,'1')
    else: 
	rawGPS(x,'1')
	
    y=ser2.readline()
    if raw==0: 
    	parseGPS(y,'2')
    else:
    	rawGPS(y,'2')
