# import gpiod

# BUTTON_LINE_OFFSET = 15

# chip0_button = gpiod.Chip("1", gpiod.Chip.OPEN_BY_NUMBER)

# button = chip0_button.get_line(BUTTON_LINE_OFFSET)
# button.request(consumer='BUTTON', type=gpiod.LINE_REQ_DIR_IN)

# print(button.consumer())


# for i in range(10):
#     print(button.get_value())


import gpiod

chip0 = gpiod.Chip("/dev/gpiochip0")
chip1 = gpiod.Chip("/dev/gpiochip1")


# line number = (char - 'A') * 8 + number
# for example: GPIO1_B2 = chip1 + 1 * 8 + 2 = 10, chip1, line 10

button = chip0.get_line(16)  # GPIO line number
button.request(consumer="button", type=gpiod.LINE_REQ_DIR_IN)

led_r = chip0.get_line(15)
led_r.request(consumer="led_r", type=gpiod.LINE_REQ_DIR_OUT)
led_b = chip1.get_line(7)
led_b.request(consumer="led_b", type=gpiod.LINE_REQ_DIR_OUT)
led_g = chip1.get_line(8)
led_g.request(consumer="led_g", type=gpiod.LINE_REQ_DIR_OUT)

value = button.get_value()
print("GPIO value:", value)

led_r.set_value(0)
led_b.set_value(0)
led_g.set_value(0)




