from includes.LLC_functions import *
# from includes.Subsystems import *
# from includes.Stepper_pin_def import *
# from includes.Subsystem_motion_sequences import *

from machine import Pin, I2C
import time
'''
    1. System basic functionalitis, tests
    2. Full feedforward control, start to end, with only the control discription
    3. 

    99. A Serial communication control mode
'''



# Test code 
time.sleep(3) # Prevent the rshell from grabbing the serial port
boot() # Initialize all pins to 0, beep for 6 times.
# while(1):
#     blink(1)




led = Pin(25, Pin.OUT)
led.on()












# #############################################
# ###### Stage 1, System initializations ######
# '''
#     About boot.py, having boot.py makes deleting files on rp2040 really slow somehow.
# '''
# time.sleep(3) # Prevent the rshell from grabbing the serial port
# boot() # Initialize all pins to 0, beep for 6 times.


# # 初始化I2C，Pico的SDA和SCL分别是GPIO20和GPIO21
# i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)

# time.sleep(5)
# # 扫描I2C总线，看看是否能找到两个Pro Mini
# devices = i2c.scan()
# print("I2C设备地址:", devices)

# # 向每个设备发送简单数据测试

# # Make sure data is less than 32 bytes


# '''
#     Notes:
#         1. Avoid I2C poor connections
#         2. Data to send in one go must be under 32 bytes

#         '''
# while(1):
#     if len(devices) == 0:
#         devices = i2c.scan()
#         print("I2C设备地址:", devices)
#         time.sleep(2)

#     if devices:
#         for device in devices:
#             # string_to_send = 'DAMN arduino {}\n'.format(device)
#             string_to_send = 'DAMN arduino 0x08'
#             # ' address {device}, HELLO!'
#             byte_data = string_to_send.encode()
#             i2c.writeto(device, byte_data)
#             print(f'Wrote to device {device}.')
#             time.sleep(2)
#     blink(2)

# #############################################
# ##### Stage 2, Control logic ######



# #############################################
# ##### Stage 3, Done ######
# pin_init()
# while(1):
#     blink(1)
#     time.sleep(1)
#     print('eepi ')
#     print()
