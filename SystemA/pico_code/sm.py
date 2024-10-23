#!/usr/bin/env python3.10-intel64
from uploader_functions.uploader_functions import *

if __name__ == '__main__':
    # port = '/dev/ttyACM0'    
    port = '/dev/cu.usbmodem14201'
    os.system("clear")
    fancy_print()
    RP2040headerString = PrintRP2040Header()

    try:
        active_serial_monitor(port, RP2040headerString)
    except KeyboardInterrupt:
        print_like_GPT('KeyboardInterrupt, exiting.')
