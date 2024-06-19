# SPDX-FileCopyrightText: Copyright (c) 2022 tinkeringtech for TinkeringTech LLC

import time
import board
import supervisor
from adafruit_bus_device.i2c_device import I2CDevice
import tinkeringtech_rda5807m


# Initialize i2c bus
# If your board does not have STEMMA_I2C(), change as appropriate.
i2c = board.STEMMA_I2C()

# Receiver i2c communication
address = 0x11
vol = 15  # Default volume
band = "FM"

rds = tinkeringtech_rda5807m.RDSParser()


# Initialize the radio classes for use.
radio_i2c = I2CDevice(i2c, address)
radio = tinkeringtech_rda5807m.Radio(radio_i2c, rds, 9030, vol)
radio.set_band("FM")  # Minimum frequency - 87 Mhz, max - 108 Mhz
radio.set_freq(9030)



while True:
    print('nonstop_kfai')