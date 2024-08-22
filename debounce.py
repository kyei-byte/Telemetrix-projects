"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,f
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from telemetrix import telemetrix

"""
Monitor a digital input pin
"""

"""
Setup a pin for digital input and monitor its changes
"""

# Set up a pin for analog input and monitor its changes
DIGITAL_PIN = 2  # arduino pin number
RED_LED = 3
GREEN_LED = 4
BLUE_LED = 5

# yet to figure out how to implement this for the debouncing. Having troubles with this.
# lastButtonState = 0
# debounceCounter = 0
# debounceThreshold = 4
lastPressed = 0
lastReleased = 0
debounceTime = 0.100



# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

def set_leds(mode):         # I did this upon your advice and explanation  # function to set the led colors
    if mode == 0:
        board.digital_write(RED_LED, 1)
        print("Red LED: on")
        board.digital_write(GREEN_LED, 0)
        print("Green LED: off")
        board.digital_write(BLUE_LED, 0)
        print("Blue LED: off\n")


    elif mode == 1:
        board.digital_write(GREEN_LED, 1)
        print("Green: on")
        board.digital_write(RED_LED, 0)
        print("Red LED: off")
        board.digital_write(BLUE_LED, 0)
        print("Blue LED: off\n")

    elif mode == 2:
        board.digital_write(BLUE_LED, 1)  # BLUE LED ON
        print("Blue LED: on")
        board.digital_write(RED_LED, 0)  # RED LED OFF
        print("Red LED: off")
        board.digital_write(GREEN_LED, 0)  # GREEN LED OFF
        print("Yellow LED: off")


def the_callback(data):
    global mode, lastPressed, lastReleased, debounceTime
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin, current reported value, pin_mode, timestamp]
    """
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    print(f'Pin Mode: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')
    now = time.time()

    if (data[CB_VALUE] == 1):
        lastReleased = now

    if (data[CB_VALUE] == 0):
        lastPressed = now

    if lastPressed > lastReleased + debounceTime:
        mode = (mode + 1) % 3

    # debounceCounter += 1
    print("Button pressed to switch LED!")

    lastPressed = now

    set_leds(mode)




# Beginning of main function
board = telemetrix.Telemetrix()


# Setup part

board.set_pin_mode_digital_input_pullup(DIGITAL_PIN, the_callback)
# time.sleep(1)
# my_board.disable_all_reporting()
# time.sleep(4)
# my_board.enable_digital_reporting(12)

# time.sleep(3)
# my_board.enable_digital_reporting(pin)
# time.sleep(1)

mode = 0

# Loop function
print('Enter Control-C to quit.')
# my_board.enable_digital_reporting(12)
try:
 while True:

         time.sleep(1)



except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)