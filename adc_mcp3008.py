import sys
import time

from telemetrix import telemetrix


class MCP3008DAC:
    # Constants
    MCP3008_SPI_MAX_5V = 3600000    # SPI MAX Value on 5V pin
    MCP3008_SPI_MAX_3V = 1350000    # SPI MAX Value on 3V pin
    MCP3008_SPI_MAX = MCP3008_SPI_MAX_3V  # SPI MAX Value
    MCP3008_SPI_ORDER = 0           # SPI bit order
    MCP3008_SPI_MODE = 0            # SPI mode
    MCP3008_SPI_FREQ = 1000000      # SPI clock speed

    def __init__(self, board, cs_pin):

        self.board = board
        self.cs_pin = cs_pin

        # Initializing spi
        self.board.set_pin_mode_spi()
        self.board.set_pin_mode_digital_output(cs_pin)

    def read_adc(self, channel):

        if channel < 0 or channel > 7:
            raise ValueError("Channel must be between 0 and 7")

        # command for MCP3008
        start_bit = 1
        end_bit = 1
        command = [start_bit, (end_bit << 7) | (channel << 4), 0]   # right??

        # setting Channel Select low to start comm
        self.board.digital_write(self.cs_pin, 0)
        time.sleep(0.001)

        # setting the spi transfer
        response = self.board.spi_transfer(command)

        # setting Channel Select high to end com
        self.board.digital_write(self.cs_pin, 1)

        # setting the response to get the adc value
        adc_value = ((response[1] & 3) << 8)    # right??

        return adc_value
