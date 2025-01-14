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
        self.value = 0

        # Initializing spi here
        self.board.set_pin_mode_spi()
        self.board.set_pin_mode_digital_output(cs_pin)

    def read_callback(self, report):
        if len(report) >= 5:          # to ensure data is complete ??
            msb = (report[3] & 0b00000011) << 8   # extract values from D9 and D8
            lsb = report[4]                       # extract values from d7-d0
            self.value = msb | lsb                # combining to get 10-bit value
            self.value = report[4]
            print("Callback ADC Value:, {self.value}")

    def read_adc(self, channel):

        if channel < 0 or channel > 7:
            raise ValueError("Channel must be between 0 and 7")

        # constructing command byte for MCP3008 and setting start bit and diff mode to 1's
        command = 0b00011000 | (channel << 1)

        # chip select has to be low to start comm so setting CS to low = 0 to start comm
        self.board.digital_write(self.cs_pin, 0)
        time.sleep(0.001)     # for a bit of delay

        # changing this setting from spi transfer to spi blocking and setting up respective parameters
        response = self.board.spi_read_blocking(register_selection=command, number_of_bytes_to_read=2, call_back=self.read_callback,
                                                enable_read_bit=False)

        # setting chip select high=1 to end comm
        self.board.digital_write(self.cs_pin, 1)

        # setting the response most and least significant bit to get the adc value 10-bit
        msb = (response[0] & 0b00000011) << 8   # to extract upper bits, D9 and D8
        lsb = response[1]                       # to extract lower bits, D7 to D0
        adc_value = msb | lsb                   # this to get the 10-bit

        return adc_value


