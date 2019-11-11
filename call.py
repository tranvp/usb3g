import serial
#from curses import ascii
# since we need ascii code from CTRL-Z
import time

# here we are testing sending an SMS via virtual serial port ttyUSB0 that was created by a USB serial modem

phonenumber = "+84906270984"#enter phone number to send SMS to e.g. "+441234123123"
ser = serial.Serial('COM42', 460800, timeout=1)
# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to

ser.write("AT+CPIN?\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)


ser.write("WAIT=1\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)


ser.write("AT+CSQ\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)


ser.write("AT+COPS?\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("WAIT=3\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)


ser.write("AT+CREG?\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)


ser.write("WAIT=3\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("ATD0906270984;\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)
time.sleep(10)
ser.write("AT^DDSETEX=2;\r\n")
time.sleep(60)

ser.write("WAIT=10\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("AT+CVHU=0\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

ser.write("ATH\r\n")
# send AT to the ttyUSB0 virtual serial port
line = ser.readline()
print(line)

time.sleep(10)
# wait 10 seconds
print ser.readline()
print ser.readline()
print ser.readline()
print ser.readline()
