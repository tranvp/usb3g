import serial
#from curses import ascii
# since we need ascii code from CTRL-Z
import time

# here we are testing sending an SMS via virtual serial port ttyUSB0 that was created by a USB serial modem

#phonenumber = "+84906270984"#enter phone number to send SMS to e.g. "+441234123123"
ser = serial.Serial('COM42', 460800, timeout=1)
# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to

ser.write("AT+CMGF=0\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("WAIT=1\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("AT+CUSD=1,*112#,15\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

time.sleep(10)
# wait 10 seconds
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
