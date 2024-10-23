#!/usr/bin/env python3
from uploader_functions.uploader_functions import *


if __name__ == "__main__":
    os.system('sudo pigpiod')
    argv = sys.argv

    if len(argv) == 1:
        activate_serial_monitor = False 
    elif len(argv) > 2:
        print_like_GPT('Invalid arguments\n', bcolors.color256(fg=229))
        os._exit(0)
    elif argv[1] == '-help':
        print_like_GPT('Pass in \'-sm\' to active serial monitor after rebooting.\n', bcolors.color256(fg=229))
        print_like_GPT('Pass in nothing to just upload.\n', bcolors.color256(fg=229))
        os._exit(0)
    elif argv[1] == '-sm':
        activate_serial_monitor = True
    else:
        print_like_GPT('Invalid arguments\n', bcolors.color256(fg=229))
        os._exit(0)

    RPi4BHeaderString = PrintRPi4BHeader()
    print_like_GPT(RPi4BHeaderString + 'Rebooting the RP2040\n', bcolors.color256(fg=229))
    reboot_pico(RPi4BHeaderString)
    print_like_GPT(RPi4BHeaderString + "Done............\n", bcolors.color256(fg=229))


    if activate_serial_monitor:
        port = '/dev/ttyACM0'    
        os.system("clear")
        fancy_print()
        RP2040headerString = PrintRP2040Header()

        active_serial_monitor(port, RP2040headerString)
