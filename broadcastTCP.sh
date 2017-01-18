#!/bin/bash
sudo service gpsd stop
sudo socat tcp-l:3000,reuseaddr,fork file:/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AH01CFIG-if00-port0,nonblock,b9600,iexten=0,raw &
sudo socat tcp-l:4000,reuseaddr,fork file:/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AE01F64S-if00-port0,nonblock,b9600,iexten=0,raw &


#sudo socat tcp-l:3000,reuseaddr,fork file:/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AH01CFIG-if00-port0,nonblock,waitlock=/var/run/ttyAMA0.lock,b9600,iext$
#sudo socat tcp-l:4000,reuseaddr,fork file:/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AE01F64S-if00-port0,nonblock,waitlock=/var/run/ttyAMA0.lock,b9600,iext$


