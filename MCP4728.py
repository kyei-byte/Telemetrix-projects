import sys
import time
from telemetrix import telemetrix

_MCP4728_MULTI_IR_CMD = 0x40
_MCP4728_ADDR = 0x60  # DEFAULT address
_MCP4728_CMD_UPDATE = 0x00  # mcp4728 command for updating dac values???
_MCP4728_CMD_EEPROM = 0x50  # command for saving to eeprom   Is 50 the right value??
_MCP4728_MULTI_WRITE_CMD = 0x40  # Don't know if this value is right??


class MCP4728:
    """Library for MCP4728 I2C 12-bit Quad DAC using telemetrix.

    :param board: The Telemetrix board the MCP4728 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x60`
    """

    def __init__(self, board, address: int = 0x60) -> None:  # DONE WITH THIS SECTION I GUESS??
        self.board = board
        self.addr = address  # moved this here
        self.board.set_pin_mode_i2c()  # FOR I2C COMs

        # SETTING CHANNELS AND SPLITTING BITS INTO HIGH AND LOW

    def set_channel_value(self, channel: int, value: int, vref: int = 0, gain: int = 0, pd: int = 0,
                          udac: int = 0) -> None:

        # high_byte = (channel << 4) | (value >> 8)
        # low_byte = value & 0xFF   # Lower bits
        # command = [high_byte, low_byte]  # getting rid of this
        command = bytearray(3)        # to create sequence of bytes
        command[0] = (_MCP4728_MULTI_WRITE_CMD | (channel << 1) | udac) & 0xFF
        command[1] = ((value >> 4) & 0xFF) | (vref << 7) | (pd << 5) | (gain << 4)   # problem here
        command[2] = (value & 0x0F) << 4

        if not 0 <= channel <= 3:
            raise ValueError("channel should be between 0 and 3")

        if not 0 <= value <= 4095:  # TO ENSURE CHANNEL IS WITHIN RANGE
            raise ValueError("value should be between 0 and 4095")

        self.board.i2c_write(self.addr, command)  # SAVED ON MEM
        print("channel not complete yet")

    def fast_write(self, value_A: int, value_B: int, value_C: int, value_D: int) -> None:
        # Insert your code here
        # value  = [value_A, value_B, value_C, value_D]  # values for dac channels. right??
        for value in [value_A, value_B, value_C, value_D]:  # for all channels
            if not 0 <= value <= 4095:
                raise ValueError("All values should be within 0 and 4095")  # to ensure within range. right?
        # print(f'Value D\n{value_A:016b}')
        # setting command for dac channels. Am I right??
        # command = [
        #
        #     # CHANNEL A
        #     (value_A >> 8) & 0xF, (value_A & 0xFF),
        #     # CHANNEL B
        #     (value_B >> 8) & 0xF, (value_B & 0xFF),
        #     # CHANNEL C
        #     (value_C >> 8) & 0xF, (value_C & 0xFF),
        #     # CHANNEL D
        #     (value_D >> 8) & 0xF, (value_D & 0xFF)
        # ]

        command = bytearray(9)
        command[0] = (_MCP4728_MULTI_WRITE_CMD)
        command[1] = (value_A >> 4) & 0xFF
        command[2] = (value_A & 0x0F) << 4
        command[3] = (value_B >> 4) & 0xFF
        command[4] = (value_B & 0x0F) << 4
        command[5] = (value_C >> 4) & 0xFF
        command[6] = (value_C & 0x0F) << 4
        command[7] = (value_D >> 4) & 0xFF
        command[8] = (value_D & 0x0F) << 4

        self.board.i2c_write(self.addr, command)  # MOVED THIS HERE
        # command1 = _MCP4728_MULTI_IR_CMD
        # command.append(command1)
        print("fast write completed")

    def multi_write_dac(self, value_A: int, value_B: int, value_C: int, value_D: int) -> None:
        for value in [value_A, value_B, value_C, value_D]:  # for all channels
            if not 0 <= value <= 4095:
                raise ValueError("for all values be within 0 and 4095")

            command = bytearray(9)
            command[0] = (_MCP4728_MULTI_WRITE_CMD)
            command[1] = (value_A >> 4) & 0xFF
            command[2] = (value_A & 0x0F) << 4
            command[3] = (value_B >> 4) & 0xFF
            command[4] = (value_B & 0x0F) << 4
            command[5] = (value_C >> 4) & 0xFF
            command[6] = (value_C & 0x0F) << 4
            command[7] = (value_D >> 4) & 0xFF
            command[8] = (value_D & 0x0F) << 4

    # command = [
    #
    #       _MCP4728_MULTI_WRITE_CMD,
    #       # CHANNEL A
    #       (value_A >> 8) & 0x0F, (value_A & 0xFF),
    #       # CHANNEL B
    #       (value_B >> 4) & 0xFF, (value_B & 0xFF),
    #       # CHANNEL C
    #       (value_C >> 4) & 0xFF, (value_C & 0xFF),
    #       # CHANNEL D
    #       (value_D >> 4) & 0xFF, (value_D & 0xFF)
    #     ]

        self.board.i2c_write(self.addr, command)
        print("multi write dac completed")

    # Extra credit, in case you want to try something new
    # def set_channel_value(self, channel: int, value: int, new_vref: int, new_gain: int, new_pd_mode: int, udac: bool = 0) -> None:
    # print("Not implemented yet")
    # Insert code here
    def save_to_EEPROM(self) -> None:  # DONE WITH THIS SECTION I GUESS??
        # I just put this here but don't know if it's write. This to save settings to eeprom
        command = [_MCP4728_CMD_EEPROM]  # WHAT MIGHT BE THE ISSUE HERE???
        self.board.i2c_write(self.addr, command)
        print("save implement done")
        # Insert your code here
