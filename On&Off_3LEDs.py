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
DIGITAL_PIN = 12  # arduino pin number
RED_LED = 3       # arduino pin for Red LED
YELLOW_LED = 4    # arduino pin for Yellow LED
GREEN_LED = 5     # arduino pin for Green LED

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3


def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin, current reported value, pin_mode, timestamp]
    """
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    print(f'Pin Mode: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')


def digital_in(my_board, pin):
    # SETUP WITH THE PIN MODE

    my_board.set_pin_mode_digital_input(pin, the_callback)
    # time.sleep(1)
    # my_board.disable_all_reporting()
    # time.sleep(4)
    # my_board.enable_digital_reporting(12)

    # time.sleep(3)
    # my_board.enable_digital_reporting(pin)
    # time.sleep(1)


    # LOOP FUNCTION
    print('Enter Control-C to quit.')
    # my_board.enable_digital_reporting(12)

    # COUNTER FOR NUMBER OF CYCLES
    cycles = 0
    max_cycles = 3
    try:
        while cycles < max_cycles:

        #while True:
            #time.sleep(1)
            my_board.digital_write(RED_LED, 1)    # RED LED ON
            print("Red LED on")
            time.sleep(2)
            my_board.digital_write(RED_LED, 0)    # RED LED OFF
            print("Red LED off")
            time.sleep(0.5)
            my_board.digital_write(YELLOW_LED, 1)  # YELLOW LED ON
            print("YELLOW LED on")
            time.sleep(2)
            my_board.digital_write(YELLOW_LED, 0)  # YELLOW LED OFF
            time.sleep(0.5)
            my_board.digital_write(GREEN_LED, 1)  # GREEN LED ON
            print("Green LED")
            time.sleep(2)
            my_board.digital_write(GREEN_LED, 0)  # GREEN LED OFF
            time.sleep(0.5)


            cycles += 1






    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)


board = telemetrix.Telemetrix()

try:
    digital_in(board, DIGITAL_PIN)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)