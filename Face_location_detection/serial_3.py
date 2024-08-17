import serial
import os
import time
import numpy as np
port = '/dev/cu.usbserial-00000000'

arduino = serial.Serial(port=port,  baudrate=115200, timeout=.1)
time.sleep(2)
def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data

def readloop():
    try:
        value = arduino.readline()
        value = value.decode()
        # time.sleep(0.02)
        print(f'received value is: {value}')

    except KeyboardInterrupt:
        print('\n\nKeyboard interrputed, exiting.\n')
        os._exit(0)


data_header_a = 'a' + '\n'
data_header_b = 'b'
read_header = 'r' + '\n'
ON = 'A'
OFF = 'B'
def send_2_data(data1, data2):
    try:
        # _ = arduino.readline()
        if arduino.isOpen():
            _ = arduino.read()
            # arduino.write(bytes(data_header_a,  'utf-8'))
            # data1 = str(data1) + '\n'
            # arduino.write(bytes(data1,  'utf-8'))

            # time.sleep(0.01)

            # arduino.write(bytes(data_header_b,  'utf-8'))
            # data2 = str(data2) + '\n'
            # arduino.write(bytes(data2,  'utf-8'))

            # arduino.write(bytes(ON,  'utf-8'))
            # # data2 = str(data2) + '\n'
            # # arduino.write(bytes(data2,  'utf-8'))
            # received_data = arduino.readline()
            # # received_data = received_data.decode()
            # print(f'r{received_data}')

            # # time.sleep(1)
            # arduino.write(bytes(OFF,  'utf-8'))
            # # data2 = str(data2) + '\n'
            # # arduino.write(bytes(data2,  'utf-8'))
            # received_data = arduino.readline()
            # # received_data = received_data.decode()
            # print(f'r{received_data}')
            # # time.sleep(1)

            arduino.write(bytes(ON,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')

            time.sleep(.1)
            arduino.write(bytes(OFF,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            time.sleep(.1)

    except KeyboardInterrupt:
        print('\n\nKeyboard interrputed, exiting.\n')
        os._exit(0)

ON = 'A'
OFF = 'B'
data_header_a = 'C'
data_header_b = 'D'
read_header = 'R'
def send_2_data_2(data1, data2):
    data1 = str(data1)
    data2 = str(data2)
    try:
        # _ = arduino.readline()
        if arduino.isOpen():
            _ = arduino.read()
            print('Spining')
            arduino.write(bytes(ON,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            time.sleep(.01)

            arduino.write(bytes(OFF,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            time.sleep(.01)

            arduino.write(bytes(data_header_a,  'utf-8'))
            arduino.write(bytes(data1,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            time.sleep(.01)

            arduino.write(bytes(data_header_b,  'utf-8'))
            arduino.write(bytes(data2,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            time.sleep(.01)

            # arduino.write(bytes(read_header,  'utf-8'))
            # received_data = arduino.readline()
            # print(f'r{received_data}')
            # time.sleep(.01)


    except KeyboardInterrupt:
        print('\n\nKeyboard interrputed, exiting.\n')
        os._exit(0)





_ = arduino.readline()


data_1 = 1.1
data_2 = 3.3 
for i in range(10):

    data_1 = data_1 + np.sin(i / 10)
    data_2 = data_2 + np.sin(i / 10)
    send_2_data_2(data_1, data_2)

# for i in range(10):
time.sleep(0.1)
_ = arduino.read_all()
_ = arduino.read_all()
_ = arduino.read_until("\n")

arduino.write(bytes(read_header,  'utf-8'))
received_data = arduino.readline()
print(f'r{received_data}')
time.sleep(.1)

arduino.write(bytes(read_header,  'utf-8'))
received_data = arduino.readline()
print(f'r{received_data}')
time.sleep(.1)

arduino.close() 
