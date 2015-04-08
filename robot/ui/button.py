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

from obsub import event
import RPi.GPIO as GPIO
import time

STATE_UP = 0
STATE_DOWN = 1

class Button(object):
    def __init__(self, pin):
        self._state = STATE_UP
        self._pin = pin

        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @event
    def OnStateChange(self, _state):
        pass

    def update(self):
        state = STATE_UP if GPIO.input(self._pin) else STATE_DOWN

        if self._state != state:
            self._state = state
            self.OnStateChange(self._state)


class UIButtonBehaviour(object):
    def __init__(self, button, press_threshold = 3):
        self._button = button
        self._lastPress = 0
        self._threshold = press_threshold

        self._button.OnStateChange += self.OnButtonStateChanged

    def __del__(self):
        self._button.OnStateChange -= self.OnButtonStateChanged

    @event
    def OnClick(self):
        pass

    @event
    def OnPress(self):
        pass

    @event
    def OnRelease(self):
        pass

    @event
    def OnLongPress(self):
        pass

    def update(self):
        self._button.update()

    def OnButtonStateChanged(self, sender, state):
        if state is STATE_DOWN:
            self.OnPress()
            self._lastPress = time.time()
        elif state is STATE_UP:
            self.OnRelease()

            if (time.time() - self._lastPress) >= self._threshold:
                self.OnLongPress()
            else:
                self.OnClick()

            self._lastPress = 0


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    def _click(sender):
        print("On Click")

    b = UIButtonBehaviour(Button(26))
    b.OnClick += _click

    while True:
        b.update()