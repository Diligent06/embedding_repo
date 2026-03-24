import sys
import signal
import os
import time
import struct

# 导入i2cdev
from i2cdev import I2C

"""
register pointer address

Configuration Register: 0x00 RW
Shunt Voltage Register: 0x01 R
Bus Voltage Register: 0x02 R
Power Register: 0x03 R
Current Register: 0x04 R
Calibration Register: 0x05 RW
Mask/Enable Register: 0x06 RW
Alert Limit Register: 0x07 RW
Manufacturer ID Register: 0xFE (Containes unique manufacturer identification number) R
Die ID Register: 0xff (contains unique die identification number) R


"""

class INA226:
    def __init__(self, bus=1, addr=0x40):
        self.i2c = I2C(addr, bus)
        self.last_register = None

        self.bus_voltage = 0.0
        self.shunt_voltage = 0.0


    def set_register(self, reg):
        if reg != self.last_register:
            self.i2c.write(bytes([reg]))
            self.last_register = reg
            
    def read_register(self, reg):
        if reg != self.last_register:
            self.set_register(reg)
        # 2. read 2 bytes
        data = self.i2c.read(2)
        print(f'read data {data}')
        # INA226 is big-endian
        return struct.unpack(">H", data)[0]

    def write_register(self, reg, value):
        data = struct.pack(">BH", reg, value)
        self.i2c.write(data)

    def read_shunt_voltage(self):
        shunt_voltage = self.read_register(0x01)
        shunt_voltage = ~(shunt_voltage - 1)
        shunt_voltage = abs(shunt_voltage) * (2.5 / 1e3)
        return shunt_voltage # unit is mV

    def read_bus_voltage(self):
        bus_voltage = self.read_register(0x02)
        bus_voltage = bus_voltage * 1.25 / 1e3
        return bus_voltage    # unit is V

    def read_shunt_current(self):
        current = self.read_register(0x04)
    
    def read_power(self):
        power = self.read_register(0x03)
    
    def read_calibration(self):
        calibration = self.read_register(0x05)
    
    def read_configuration(self):
        configuration = self.read_register(0x00)

    # current_lsb unit is A, R_shunt unit is omu
    def set_calibrate_register(self, current_lsb, R_shunt):
        CAL = int(0.00512 / (current_lsb * R_shunt))
        if CAL > 0xFFFF:
            CAL = 0xFFFF
        
        self.write_register(0x05, CAL)

    def set_configuration_register(self, value):
        pass
    
    def close(self):
        self.i2c.close()
