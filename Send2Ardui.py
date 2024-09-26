#put code here to send signal to arduino to go left or up or right or down.
#make sure its in a function so that it can be called from PersonTrack.py or like other code
import serial
direction = [None,None]
global prevdir 
prevdir = [0,0]
class Send2Ardui:
    def Send(direction):
        #initialize the serial port
        #ser = serial.Serial('COM3', 9600)
        #ser.flushInput()
        #ser.flushOutput()
        #print("Serial port initialized")
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
                if prevdir[0] < direction[0]:
                    #move right
                    print("Move right")
                if prevdir[1] > direction[1]:
                    #move up
                    print("Move up")
                if prevdir[1] < direction[1]:
                    #move down
                    print("Move down")
        except UnboundLocalError:
            print("UnboundLocalError")
        prevdir[0] = direction[0]
        prevdir[1] = direction[1]