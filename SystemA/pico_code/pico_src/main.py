from includes.LLC_functions import *
# from includes.Subsystems import *
# from includes.Stepper_pin_def import *
# from includes.Subsystem_motion_sequences import *

from machine import Pin, I2C, PWM
import time
'''
    1. System basic functionalitis, tests
    2. Full feedforward control, start to end, with only the control discription
    3. 

    99. A Serial communication control mode
'''

# Test code 
buzzer = PWM(Pin(0))

time.sleep(3) # Prevent the rshell from grabbing the serial port
boot() # Initialize all pins to 0, beep for 6 times.

motor_enable = Pin(22, Pin.OUT)

for _ in range(3):
    motor_enable.on()
    time.sleep(0.3)
    motor_enable.off()
    time.sleep(0.3)

motor_enable.on()

# 创建PWM对象来控制舵机
servo_pin_20 = PWM(Pin(20))
servo_pin_21 = PWM(Pin(21))

# 设置PWM频率为50Hz（用于舵机控制）
servo_pin_20.freq(50)
servo_pin_21.freq(50)

# 将角度转换为PWM占空比
def set_servo_angle(servo, angle):
    # 角度范围一般为 0 到 180 度
    min_duty = 1000 # 最小占空比（1ms，代表0度）
    max_duty = 9000  # 最大占空比（2ms，代表180度）
    duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    servo.duty_u16(duty)

# 示例：将舵机移动到不同角度
print('Moving the servos')
motor_enable
for i in range(10):
    print(str(i) + ': Moving. ')

    set_servo_angle(servo_pin_20, 0)    # 0度
    time.sleep(1)
    set_servo_angle(servo_pin_20, 90)   # 90度
    time.sleep(1)
    set_servo_angle(servo_pin_20, 180)  # 180度
    time.sleep(1)

    # 控制第二个舵机
    set_servo_angle(servo_pin_21, 0)   # 45度
    time.sleep(1)
    set_servo_angle(servo_pin_21, 90)   # 45度
    time.sleep(1)
    set_servo_angle(servo_pin_21, 180)   # 45度
    time.sleep(1)



motor_enable.off()








# 设置PWM频率
def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)  # 设置占空比为50%，最大值为65535
    time.sleep(duration)
    buzzer.duty_u16(0)  # 停止蜂鸣器














# 示例：播放几个音调
for _ in range(3):
    play_tone(1000, 0.1)  # 1000Hz，持续1秒
    # time.sleep(1)       # 暂停1秒
    play_tone(500, 0.1)   # 500Hz，持续1秒
    # time.sleep(1)




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
