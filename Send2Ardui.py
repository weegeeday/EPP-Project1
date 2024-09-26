#put code here to send signal to arduino to go left or up or right or down.
#make sure its in a function so that it can be called from PersonTrack.py or like other code
import serial
import time
direction = [None,None]
global prevdir 
prevdir = [0,0]

#initialize the serial port
ser = serial.Serial('COM3', 115200)
ser.flushInput()
ser.flushOutput()
#try:
    #ser2 = serial.Serial('COM4', 115200)
    #ser2.flushInput()
    #ser2.flushOutput()
#except serial.SerialException:
   # print("Serial port error")
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
                if prevdir[0] > direction[0]:
                    #move left
                    print("Move left")
                    unmapst = prevdir[0] - direction[0]
                    #steps is from 0 to 180 degrees, convesion from unmapst to steps needs to be done, unmapst is the difference in x coordinates, coords have limits that equal the camera resolution 480x640.
                    steps = int((unmapst/640)*180)
                    print(steps)
                    ser.write(bytes(steps))
                    time.sleep(1)
                if prevdir[0] < direction[0]:
                    #move right
                    print("Move right")
                    unmapst = direction[0] - prevdir[0]
                    steps = int((unmapst/640)*180)
                    ser.write(bytes(steps))
                    time.sleep(1)
                if prevdir[1] > direction[1]:
                    #move up
                    print("Move up")
                    #ser2.write(bytes(steps))
                    time.sleep(1)
                if prevdir[1] < direction[1]:
                    #move down
                    print("Move down")
                    #ser2.write(bytes(steps))
                    time.sleep(1)
        except UnboundLocalError:
            print("UnboundLocalError")
        except TypeError:
            print("TypeError")
        prevdir[0] = direction[0]
        prevdir[1] = direction[1]
        print(ser.read_all())