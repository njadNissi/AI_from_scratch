import serial, sys

# on windows it looks like COM<number>, on linux ttyUSB<number> or ttyACM<number>
port = 'COM4'
br =  9600

args = sys.argv[1:]
for i in range(0, len(args), 2):
	v = args[i : i+2]

	if v[0] == '-p':
		port = '/dev/' + v[1]
	elif v[0] == '-br':
		br = int(v[1])

print(f"Reading FROM : port={port}, Baud-Rate={br}")

ser = serial.Serial(port, br)

while True:
	bs = str(ser.readline(), 'utf-8').strip('/n/r')
	print(bs)
