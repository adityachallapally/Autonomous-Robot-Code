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

import RPi.GPIO as GPIO

from twisted.internet import task
from twisted.internet import reactor

from robot.control.controller import Robot

import robot.utils.config as config
from robot.utils.fps import FPS
from robot.ui.menu import MenuEntry, Menu
import robot.ui.display as display


class App(object):
    def __init__(self):
        self._controller = Robot()
        self._mainLoop = None
        self._uiLoop = None
        self._inputLoop = None
        self._menu = None

    def setup(self, args):
        self._controller.setup()

        self._mainLoop = task.LoopingCall(self._stepController)
        self._uiLoop = task.LoopingCall(self._stepUI)
        self._inputLoop = task.LoopingCall(self._stepInput)

        GPIO.setmode(GPIO.BCM)

        self._menu = Menu()
        self._menu.add("Top/Debug/Logging", MenuEntry("cool"))

        display.current(self._menu)


    def run(self):

        self._mainLoop.start(1.0 / config.CONFIG.get("fps", 20), now=True)
        self._uiLoop.start(1.0 / config.CONFIG.get("fps_ui", 10), now=True)
        self._inputLoop.start(1.0 / config.CONFIG.get("fps_input", 20), now=True)

        self._uiLoop

        # Start the loop
        reactor.run()

    def purge(self):
        self._controller.purge()
        display.purge()
        reactor.stop()

    def _stepController(self):
        self._controller.update()

    def _stepUI(self):
        self._menu.update()
        display.update()


    def _stepInput(self):
        pass
