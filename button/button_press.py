import Hobot.GPIO as GPIO
import time
import signal
import sys
from Hobot.GPIO.gpio import _cleanup_one, remove_event_detect
led_pin_1 = 11
led_pin_2 = 35
but_pin = 37

LONG_PRESS_THRESHOLD = 1.0  # seconds

on_rising_value = True

press_start_time = None

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(but_pin, GPIO.IN)

    print("Starting demo now! Press CTRL+C to exit")
    last_state = GPIO.LOW
    press_time = -1
    try:
        while True:
            if time.time() - press_time < 0.2:
                time.sleep(0.05)
                continue
                
            curr_value = GPIO.input(but_pin)

            if curr_value == GPIO.HIGH and last_state == GPIO.LOW:
                press_time = time.time()
                last_state = GPIO.HIGH
            
            if curr_value == GPIO.LOW and last_state == GPIO.HIGH:
                if time.time() - press_time > 1:
                    print('long press')
                else:
                    print('short press')
                last_state = GPIO.LOW

        
            time.sleep(0.05)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
