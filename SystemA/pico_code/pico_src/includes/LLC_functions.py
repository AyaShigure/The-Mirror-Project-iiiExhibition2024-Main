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
