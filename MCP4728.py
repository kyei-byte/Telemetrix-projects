import sys
import time

from telemetrix import telemetrix

_MCP4728_MULTI_IR_CMD = 0x40
_MCP4728_ADDR = 0x60         # DEFAULT address
_MCP4728_CMD_UPDATE = 0x00   # mcp4728 command for updating dac values???
_MCP4728_CMD_EEPROM = 0xFF   # command for saving to eeprom   FIND THE VALUE??


class MCP4728:
    """Library for MCP4728 I2C 12-bit Quad DAC using telemetrix.

    :param board: The Telemetrix board the MCP4728 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x60`
    """
    def __init__(self, board, address: int = 0x60) -> None:         # DONE WITH THIS SECTION I GUESS??
        self.board = board
        self.addr = address    # moved this here

        self.board.set_pin_mode_i2c()


    def set_channel_value(self, channel: int, value: int, vref: int = 0, pd: int = 0) -> None:
      high_byte = (channel << 4) | (value >> 8)
      low_byte = value & 0xFF   # LOWER 8 BITS??
    # if channel ???
    print("Not implemented yet")




    def fast_write(self, value_A: int, value_B: int, value_C: int, value_D: int) -> None:
        # Insert your code here
        # values = [value_A, value_B, value_C, value_D]  # values for dac channels. right??
        print(f'Value D\n{value_A:016b}')
        # setting command for dac channels. Am I right??
        command = [
            # CHANNEL A
            (value_A >> 8) & 0xF, (value_A & 0xFF),
            # CHANNEL B
            (value_B >> 8) & 0xF, (value_B & 0xFF),
            # CHANNEL C
            (value_C >> 8) & 0xF, (value_C & 0xFF),
            # CHANNEL D
            (value_D >> 8) & 0xF, (value_D & 0xFF)
        ]
        print(f'{command[0]:08b}{command[1]:08b}')

        self.board.i2c_write(self.addr, command)  # MOVED THIS HERE
        # command1 = _MCP4728_MULTI_IR_CMD
        # command.append(command1)
        print("Not implemented yet")

    # Extra credit, in case you want to try something new
    #def set_channel_value(self, channel: int, value: int, new_vref: int, new_gain: int, new_pd_mode: int, udac: bool = 0) -> None:
    #    print("Not implemented yet")
        # Insert your code here
    def save_to_EEPROM(self) -> None:                               # DONE WITH THIS SECTION I GUESS??
        # I just put this here but don't know if it's write. This to save settings to eeprom
        command = [_MCP4728_CMD_EEPROM]                           # WHAT MIGHT BE THE ISSUE HERE???
        self.board.i2c_write(self.addr, command)
        print("Not implemented yet")
        # Insert your code here
