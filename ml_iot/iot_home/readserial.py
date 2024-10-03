import serial

port = '/dev/ttyUSB0'
br =  9600

print(f"Raeading FROM : port={port}, Baud-Rate={br}")

ser = serial.Serial(port, br)

while True:
	bs = str(ser.readline(), 'utf-8').strip('/n/r')
	print(bs)
