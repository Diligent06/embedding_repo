import gpiod
import time
from gpiod.line import Direction, Value

button_line = 16
led_r_line = 15
led_g_line = 8


request_chip0 = gpiod.request_lines(
    "/dev/gpiochip0",
    consumer="chip0",
    config={
        15: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        ),
        16: gpiod.LineSettings(
            direction=Direction.INPUT
        )
    }
)

request_chip1 = gpiod.request_lines(
    "/dev/gpiochip1",
    consumer="chip1",
    config={
        8: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )
    }
)

start_time = 0
record_state = 0

while True:
    button_value = request_chip0.get_value(button_line)
    if button_value == Value.ACTIVE and time.time() - start_time > 3:
        start_time = time.time()
        if record_state == 0:
            record_state = 1
            request_chip0.set_value(led_r_line, Value.ACTIVE)
            request_chip1.set_value(led_g_line, Value.INACTIVE)
        else:
            record_state = 0
            request_chip0.set_value(led_r_line, Value.INACTIVE)
            request_chip1.set_value(led_g_line, Value.ACTIVE)
        
        
