import serial
import time

ser = serial.Serial("COM3", 9600)
file = "FILENAME.txt"

ser.write(b"1")
time.sleep(2)
with open(file, "w") as f:
    while ser.in_waiting:
        line = ser.readline().decode("utf-8").strip()
        print(line)
        f.write(line + "\n")

time.sleep(1)
ser.write(b"0")
while not ser.in_waiting:
    pass

print("done")
ser.close()
