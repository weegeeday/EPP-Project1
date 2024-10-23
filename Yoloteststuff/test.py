#this code can be ignored. its used for testing every now and then.


import serial
import time

def main():
    # Configure the serial connection
    ser = serial.Serial('COM7', 115200, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize

    while True:
        # Send '0' to the serial device
        ser.write(b'0')
        print("Sent: 0")

        # Wait to receive '1' from the serial device
        while True:
            if ser.in_waiting > 0:
                response = ser.read()
                if response == b'1':
                    print("Received: 1")
                    break

        # Send '90' to the serial device
        ser.write(b'75')
        print("Sent: 75")

        # Wait to receive '1' from the serial device again
        while True:
            if ser.in_waiting > 0:
                response = ser.read()
                if response == b'1':
                    print("Received: 1")
                    break

if __name__ == "__main__":
    main()