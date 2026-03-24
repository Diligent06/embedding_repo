from INA226_driver import INA226
import time

if __name__ == "__main__":
    ina = INA226(bus=5, addr=0x40)
    # ina.set_calibrate_register(0.0001, 0.010)
    ina.set_configuration_register(0b0100000100100110)
    print(f' shunt voltage is {ina.read_shunt_voltage()}')
    print(f'bus voltage is {ina.read_bus_voltage()}')
    ina.read_shunt_current()
    ina.read_power()
    ina.read_calibration()
    ina.read_configuration()
    # try:
    #     while True:
    #         vbus = ina.read_bus_voltage()
    #         vshunt = ina.read_shunt_voltage()

    #         print(f"Bus Voltage: {vbus:.3f} V")
    #         print(f"Shunt Voltage: {vshunt:.6f} V")
    #         print("------")

    #         time.sleep(1)

    # finally:
    #     ina.close()