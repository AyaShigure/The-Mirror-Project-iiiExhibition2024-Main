
import serial
import os
import time
port = '/dev/cu.usbserial-00000000'

arduino = serial.Serial(port=port,  baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data


# while True:
for i in range(30):
    num = str(i)
    try:
        # num = input("Enter a number: ")
        # if_readable = arduino.readable()
        # print(f'readable?? -> {if_readable}')

        # arduino.read

        value  = write_read(num)
        value = value.decode()
        time.sleep(0.02)
        print(f'send_num : {[num]} -> {value}')
    except KeyboardInterrupt:
        print('\n\nKeyboard interrputed, exiting.\n')
        os._exit(0)