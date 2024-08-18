import serial
import os
import time
import numpy as np

class arduino_object():
    def __init__(self, serial_port):
        try:
            self.arduino = serial.Serial(port=serial_port, baudrate=115200, timeout=.1)
            time.sleep(2)

        except:
            print('Invalid port, exiting..')
            os.exit(0)

        ## data type headers
        self.HEADER_LED_ON = 'A'
        self.HEADER_LED_OFF = 'B'
        self.HEADER_DATA_A = 'C'
        self.HEADER_DATA_B = 'D'
        self.HEADER_READ_DATA = 'R'
                
    def check_connection(self):
        writablt = self.arduino.writable()
        readable = self.arduino.readable()

        print(f'Writeable? -> {writablt}')
        print(f'Readable? -> {readable}')

    def fast_send_2_data_to_serial_dev(self, data1, data2):
        data1 = str(data1)
        data2 = str(data2)
        try:
            send_start = time.time()
            if self.arduino.isOpen():
                self.arduino.write(bytes(self.HEADER_DATA_A,  'utf-8'))
                self.arduino.write(bytes(data1,  'utf-8'))
                time.sleep(.005)
                self.arduino.write(bytes(self.HEADER_DATA_B,  'utf-8'))
                self.arduino.write(bytes(data2,  'utf-8'))
                time.sleep(.005)

            sending_FPS =  round(1/ (time.time() - send_start),2)
            # self.clear_read_buffer()
            # self.read_n_print()
            print(f'serial communication FPS = {sending_FPS} Hz')

        except KeyboardInterrupt:
            self.arduino.close()
            print('\n\nKeyboard interrputed, exiting.\n')
            os._exit(0)

    # def send_2_data_to_serial_dev(self, data1, data2):
    #     data1 = str(data1)
    #     data2 = str(data2)
    #     try:
    #         send_start = time.time()

    #         # _ = arduino.readline()
    #         if self.arduino.isOpen():
    #             _ = self.arduino.read()
    #             print('Spining')
    #             self.arduino.write(bytes(self.HEADER_LED_ON,  'utf-8'))
    #             # received_data = self.arduino.readline()
    #             # print(f'r{received_data}')
    #             time.sleep(.005)

    #             self.arduino.write(bytes(self.HEADER_LED_OFF,  'utf-8'))
    #             # received_data = self.arduino.readline()
    #             # print(f'r{received_data}')
    #             time.sleep(.005)

    #             self.arduino.write(bytes(self.HEADER_DATA_A,  'utf-8'))
    #             self.arduino.write(bytes(data1,  'utf-8'))
    #             # received_data = self.arduino.readline()
    #             # print(f'r{received_data}')
    #             time.sleep(.005)

    #             self.arduino.write(bytes(self.HEADER_DATA_B,  'utf-8'))
    #             self.arduino.write(bytes(data2,  'utf-8'))
    #             # received_data = self.arduino.readline()
    #             # print(f'r{received_data}')
    #             time.sleep(.005)
    #         sending_FPS =  round(1/ (time.time() - send_start),2)
    #         self.clear_read_buffer()
    #         self.read_n_print()
    #         print(f'serial communication FPS = {sending_FPS} Hz')

        # except KeyboardInterrupt:
        #     print('\n\nKeyboard interrputed, exiting.\n')
        #     os._exit(0)

    def read_n_print(self):
        # _ = self.arduino.read_all()
        self.arduino.write(bytes(self.HEADER_READ_DATA,  'utf-8'))
        received_data = self.arduino.readline()
        print(f'r{received_data}')

    def clear_read_buffer(self):
        _ = self.arduino.read_all()
        _ = self.arduino.readline()
        _ = self.arduino.read_until("\n")

    def close_serial_port(self):
        self.arduino.close()

def deg_to_arduino_servo_control(degree):
    # Assume that 180 / 2 = 90 as the center, this is needed to be calibrated
    center = 90
    servo_command = center + degree 
    return servo_command

def test_run():
    port = '/dev/cu.usbserial-00000000'
    arduinoObj = arduino_object(port)

    arduinoObj.clear_read_buffer()

    data_1 = 1.1
    data_2 = 3.3 
    for i in range(10):
        data_1 = data_1 + i
        data_2 = data_2 + i
        arduinoObj.send_2_data_to_serial_dev(data_1, data_2)

    # for i in range(10):
    time.sleep(0.1)
    # arduinoObj.clear_read_buffer()

    for i in range(5):
        arduinoObj.clear_read_buffer()  

        arduinoObj.read_n_print()
        time.sleep(.1)


    arduinoObj.close_serial_port()


# test_run()