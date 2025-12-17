import serial
import time

ser = serial.Serial("COM3", 115200) # change COM3 to your Arduino's serial port
file = "123456789.txt" # specify your file name here

ser.write(b"1") # signal to start sending data
time.sleep(1) # wait for the Arduino to send data
with open(file, "w") as f:
    while True:
        if ser.in_waiting:
            s =  ser.readline().decode("utf-8").strip()
            if s == "A": # end of file signal
                break
            line = s
            print(line)
            f.write(line + "\n")

time.sleep(1) # wait before sending the next signal
ser.write(b"0") # signal to clear the file in SD card
while not ser.in_waiting: # wait for the Arduino to send "done" signal
    pass

print("done")
ser.close()
