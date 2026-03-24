#!/usr/bin/env python3

################################################################################
# Copyright (c) 2024,D-Robotics.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import sys
import signal
import Hobot.GPIO as GPIO
import time


def signal_handler(signal, frame):
    sys.exit(0)

led_pin_list = [16, 18, 22, 26]

# 禁用警告信息
GPIO.setwarnings(False)

def main():
    # 设置管脚编码模式为硬件编号 BOARD
    GPIO.setmode(GPIO.BOARD)
    for led_pin in led_pin_list:
        GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output

    # Initial state for LEDs:
    for led_pin in led_pin_list:
        GPIO.output(led_pin, GPIO.LOW)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
