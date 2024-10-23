import serial
import time
direction = [None,None]
global prevdir 
prevdir = [0,0]
try:
    ser = serial.Serial('COM7', 115200, timeout=0.9) #one arduino for horizontal, one for vertical, cus like just write the motors to the same.
    ser2 = serial.Serial('COM11', 115200)
except serial.SerialException:
    print("Serial port error")
    exit()
print("Serial port initialized")
steps = 0
class Send2Ardui:
    def Send(direction):
        try:
            if direction == None:
                print("No direction")
                return
            if prevdir == direction:
                print("No change in direction")
                return
            if prevdir != direction:
                print("Change in direction")
                print(direction[0])
                val = str(direction[0])
                ser.write(bytes(val,encoding='ascii')) #send the angle to the arduino
                print(bytes(val,encoding='ascii'))
                time.sleep(1)
                print(direction[1])
                ser2.write(bytes(direction[1]))
                time.sleep(1)
        except UnboundLocalError:
            print("UnboundLocalError")
        except TypeError:
            print("TypeError")
        prevdir[0] = direction[0]
        prevdir[1] = direction[1]