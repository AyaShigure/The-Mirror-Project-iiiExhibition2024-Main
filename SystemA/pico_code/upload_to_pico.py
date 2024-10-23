#!/usr/bin/env python3.10-intel64
from uploader_functions.uploader_functions import *


'''
    1. Delete all files on pico
    2. Sync the file trees from local to pico (main.py and the ./includes)
    3. Active 
'''

# Operation mode:
# Preset test system mode ( Move everything )
# Emergency stop


if __name__ == "__main__":
    # os.system('sudo pigpiod') # Active pi gpio
    argv = sys.argv

    if len(argv) == 1:
        activate_serial_monitor = False 
    elif len(argv) > 2:
        print_like_GPT('Invalid arguments\n', bcolors.color256(fg=229))
        os._exit(0)
    elif argv[1] == '-help':
        print_like_GPT('Pass in \'-sm\' to active serial monitor after uploading.\n', bcolors.color256(fg=229))
        print_like_GPT('Pass in nothing to just upload.\n', bcolors.color256(fg=229))
        os._exit(0)
    elif argv[1] == '-sm':
        activate_serial_monitor = True
    else:
        print_like_GPT('Invalid arguments\n', bcolors.color256(fg=229))
        os._exit(0)

    os.system("clear")
    # port = '/dev/ttyACM0'
    port = '/dev/cu.usbmodem14201'

    MacBookHeaderString = PrintMacBookHeader()


    # Upload via rshell
    print_like_GPT(MacBookHeaderString + 'Clearing the existing file tree.\n', bcolors.color256(fg=229))
    os.system(f"rshell -p {port} rm -r /pyboard/*")

    print_like_GPT(MacBookHeaderString + 'Uploading the new file tree.\n', bcolors.color256(fg=229))
    os.system(f"rshell -p {port} rsync ./pico_src/ /pyboard/")
    # os.system(f"rshell -p {port} cp ./pico_src/main.py /pyboard/")
    # print_like_GPT(MacBookHeaderString + 'Rebooting the RP2040\n', bcolors.color256(fg=229))
    # reboot_pico(MacBookHeaderString)
    print_like_GPT(MacBookHeaderString + "Done............\n", bcolors.color256(fg=229))


    if activate_serial_monitor:
        os.system("clear")
        fancy_print()
        RP2040headerString = PrintRP2040Header()

        active_serial_monitor(port, RP2040headerString)
