from .bcolors import *
import datetime
import time
import pyfiglet
import serial
# import pigpio
import os
import sys


'''
    IMPORTANT:
        This function set is for uploading /pico_src to RP2040.
        Do not upload this file to RP2040.

'''
def fancy_print():
    ascii_art = pyfiglet.figlet_format("The Mirror", font="big")
    print_like_GPT(ascii_art)
    print()
    # print_like_GPT('[Created by ISEI & AZUL & Aya at The University of Tokyo]', bcolors.OKCYAN)
    print()

# Utilities
def PrintRP2040Header():
    headerString = '[' + 'RP2040' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    print_like_GPT(headerString + 'Initiallizing\n', bcolors.color256(fg=154))
    return headerString

def PrintMacBookHeader():
    headerString = '[' + 'MacBook Pro 2019 _ Aya' + ' | '+ f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' + '] '
    print_like_GPT(headerString + 'Initiallizing\n', bcolors.color256(fg=229))
    return headerString

def print_like_GPT(text, color=bcolors.ENDC):
    for i,char in enumerate(text):
        print(f"{color}{char}\u2588{bcolors.ENDC}", end="", flush=True)
        time.sleep(0.003)

        if i < len(text) - 1:
            print('\b \b', end='', flush=True)
    time.sleep(0.5) 

    print('\b \b', end='', flush=True) 


def active_serial_monitor(port, headerString):
    time.sleep(2)
    ser = serial.Serial(port, 115200, timeout=1)

    print_like_GPT(headerString + "Ready...\n\n",bcolors.WARNING)

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print_like_GPT(headerString + f"{line}\n",  bcolors.color256(fg=154))
            # ser.flushInput()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print_like_GPT('KeyboardInterrupt, exiting.')        
    finally:
        ser.close()