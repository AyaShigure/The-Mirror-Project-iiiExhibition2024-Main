from machine import Pin, PWM, ADC
import time

# This function set is for direct hardware control, the most basic functions

def pin_init():
    for i in range(26):
        pin = Pin(i, Pin.OUT)
        pin.off() 

def blink(count):
    led = Pin(25, Pin.OUT)
    for i in range(count):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
        
def boot():
    pin_init()
    blink(6)



#######################################
buzzer = PWM(Pin(0))

# 设置音符频率
tones = {
    'C4': 261,
    'D4': 293,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523
}


# 设置音符播放函数
def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)  # 50%占空比
    time.sleep(duration)
    buzzer.duty_u16(0)  # 停止音调
    time.sleep(0.05)  # 短暂暂停

# 播放欢乐颂片段
def play_song():
    melody = [
        ('E4', 0.5), ('E4', 0.5), ('F4', 0.5), ('G4', 0.5),
        ('G4', 0.5), ('F4', 0.5), ('E4', 0.5), ('D4', 0.5),
        ('C4', 0.5), ('C4', 0.5), ('D4', 0.5), ('E4', 0.5),
        ('E4', 0.75), ('D4', 0.25), ('D4', 1.0)
    ]

    for note, duration in melody:
        if note in tones:
            play_tone(tones[note], duration)

# 播放曲子
# play_song()