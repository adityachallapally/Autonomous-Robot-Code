# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 Björn Larsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import Adafruit_CharLCD as LCD
import time

# Pin configuration
__lcd_rs        = 19
__lcd_en        = 13
__lcd_d4        = 6
__lcd_d5        = 5
__lcd_d6        = 12
__lcd_d7        = 25
__lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
__lcd_columns = 16
__lcd_rows    = 2

__lcd = LCD.Adafruit_CharLCD(__lcd_rs, __lcd_en, __lcd_d4, __lcd_d5, __lcd_d6, __lcd_d7,
                                                        __lcd_columns, __lcd_rows, __lcd_backlight)

__currentTarget = None
__currentBuffer = ""
__last_update = 0

def current(current):
    global __currentTarget
    __currentTarget = current

def update():
    global __currentBuffer
    global __last_update

    if __currentTarget:
        if (time.time() - __last_update) > 0.4:
            __last_update = time.time()

            r = __currentTarget.render()
            if r != __currentBuffer:
                __currentBuffer = r
                __lcd.clear()
                __lcd.message(__currentTarget.render())

def purge():
    __lcd.clear()